"""
High Level Operations for every infrastructure
"""
from common.exceptions import ProfileNotFound
from common.exceptions import ResourcesNotAvailable
from common.exceptions import PlatformDoesNotExist
from common.sessions import Sessions
from common.platform import Platform

from urllib2 import URLError
from threading import Thread
import uuid
import suds
import time
import logging

class CallBackThread(Thread):
    def __init__(self, platform, core_session_id, core_ip, implementor, logger):
        Thread.__init__(self)
	self.platform = platform
	self.core_session_id = core_session_id
	self.core_ip = core_ip
	self.implementor = implementor
	self.logger = logger

    def run(self):
        """
	This function will run inside a thread and will check the deployment status.
	Once the deployment is finished, it will call the core with the endpoint.
	Input: core_session_id, core_ip
	Output: void
	"""
	try:
           client = suds.client.Client('http://' + self.core_ip + ':8080/axis2/services/CoreServices?wsdl', cache=None)
	except URLError as u:
	   self.logger.debug("Unavailable CallBack Server...")
	   return
        
	while (self.implementor.allocation_status(self.platform) == "BUILDING"):
	   self.logger.debug('Waiting to reply for core_session_id %s to %s.', self.core_session_id, self.core_ip)
	   time.sleep(15)
	     
	if self.implementor.allocation_status(self.platform) == "CREATED":
	   client.service.deployCallback(self.core_session_id, self.platform.get_endpoint())
	else:
           client.service.deployCallback(self.core_session_id, "FAILED")
	return    

class InfrastructureAbstraction:
    def __init__ (self, implementor, profiles):
        self.implementor = implementor
        self.profiles = profiles
        self.sessions = Sessions()

	# Configure Logging
	logging.basicConfig(level=logging.INFO)
	self.logger = logging.getLogger(__name__)


    def get_profile(self, profile_id):
        for profile in self.profiles.keys():
            if profile_id == self.profiles[profile]['id']:
               return self.profiles[profile]
        raise ProfileNotFound(profile_id, self.profiles)

    def check_platform_availability(self, profile_id):
        """
        Not all profiles are readly available.
        For example, a cluster profile may have to wait on queue
        for instantiation. In case of cloud profiles, this method is not used.
        Should it be only on the cluster abstractions?
        True or False. Will not make reservations, at least for now.
        profile_id -- the desired profile.
        """
        profile = self.get_profile(profile_id)
        available =  self.implementor.verify_profile_availability(profile)
        return available

    def create_platform(self, profile_id):
        """
        A platform is a container+infrastructure. This method should allocate
        the resources and deploy the container.
        profile_id -- the desired profile.
        """
        profile = self.get_profile(profile_id)
        platform_id = uuid.uuid4()
        platform = Platform(id = platform_id, profile_id = profile_id,
                            allocation_id = 0, endpoint = "NO_ENDPOINT",
                            status = "BUILDING" )
        self.sessions.add_platform(platform)
        try:
           self.implementor.allocate_resources(platform, profile)
        except ResourcesNotAvailable as e:
           return 0
        return platform_id

    def create_platform_callback(self, profile_id, core_session_id, remote_ip):
        """
        A platform is a container+infrastructure. This method should allocate
        the resources and deploy the container.
        Input: profile_id, core_session_id, remote_ip for callback
        Output: the platform_id, which is the same of core_session_id
        """
	self.logger.debug('profile_id: %s, core_session_id: %s, remote_ip: %s', profile_id, core_session_id, remote_ip)
        profile = self.get_profile(int(profile_id))
        platform = Platform(id = core_session_id, profile_id = profile_id,
                            allocation_id = 0, endpoint = "NO_ENDPOINT",
                            status = "BUILDING" )
        self.sessions.add_platform(platform)
        try:
           self.implementor.allocate_resources(platform, profile)
        except ResourcesNotAvailable as e:
           return 0
        # Thread invocation
	callback_thread = CallBackThread(platform, core_session_id, remote_ip, self.implementor, self.logger)
	callback_thread.start()
        return core_session_id

    def get_available_platforms(self):
        """
        Returns a dictionary of all instantiated platforms:
        (platform_id, profile_id)
        """
        platforms_ids = self.sessions.get_platform_list()
        return dict( (id, self.sessions.get_platform(id).get_profile_id()) for id in platforms_ids if self.sessions.get_platform(id).get_status() != "DESTROYED" )

    def get_available_platforms_endpoints(self):
        """
	Returns a dictionary of all instantiated platforms endpoints:
	(platform_id, endpoint)
	"""
        platforms_ids = self.sessions.get_platform_list()
        return dict( (id, self.sessions.get_platform(id).get_endpoint()) for id in platforms_ids if self.sessions.get_platform(id).get_status() != "DESTROYED" )

    def platform_status(self, platform_id):
        """
        The platform status will be BUILDING, CREATED, DESTROYED, FAILED
        platform_id -- the id of the platform
        """
	_id = platform_id
	try :
	   platform_id = uuid.UUID(platform_id)
	except ValueError as v:
	   self.logger.debug("Platform ID is not UUID, created by callback...")
	   platform_id = _id
	except AttributeError as v:
	   self.logger.debug("Platform ID already is UUID")
	   platform_id = _id
        platform = self.sessions.get_platform(platform_id)
        return self.implementor.allocation_status(platform)

    def get_platform_endpoint(self, platform_id):
        """
        Returns the endpoint.
        platform_id -- the id of the platform
        """
	_id = platform_id
	try :
           platform_id = uuid.UUID(platform_id)
        except AttributeError as v:
	   self.logger.debug("Platform ID already is UUID")
	   platform_id = _id
        platform = self.sessions.get_platform(platform_id)
        return platform.get_endpoint()

    def destroy_platform(self, platform_id):
        """
        Destroy the platform.
        platform_id -- the id of the platform
        """
	_id = platform_id
	try :
           platform_id = uuid.UUID(platform_id)
        except ValueError as v:
	   self.logger.debug("Platform ID is not UUID, created by callback...")
	   platform_id = _id
	except AttributeError as v:
	   self.logger.debug("Platform ID already is UUID")
	   platform_id = _id
   
        try :
           platform = self.sessions.get_platform(platform_id)
        except PlatformDoesNotExist as e:
           self.logger.info("Platform does not exist.")
           return 0

        deallocation_status = self.implementor.deallocate_resources(platform)
	self.sessions.remove_platform(platform_id)
        return deallocation_status
 
    def destroy_platform_by_endpoint(self, endpoint):
        """
	Destroy the platform with the corresponding endpoint.
	Input: the endpoint
	Output: the status of the deallocation
	"""
	self.logger.info("Destroying platform with endpoint: " + endpoint);
        platform_id = None  
        for id in self.sessions.get_platform_list():
	    _endpoint = self.sessions.get_platform(id).get_endpoint()   
	    if (endpoint == _endpoint):
	        platform_id = id

	if (platform_id == None):
	    self.logger.info("Platform not found for endpoint: " + endpoint)
	    return "NOTFOUND"
	
        return self.destroy_platform(platform_id)

