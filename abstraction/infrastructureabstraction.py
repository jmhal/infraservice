"""
High Level Operations for every infrastructure
"""
from common.exceptions import ProfileNotFound
from common.exceptions import ResourcesNotAvailable
from common.exceptions import PlatformDoesNotExist
from common.sessions import Sessions
from common.platform import Platform
import uuid

class InfrastructureAbstraction:
    def __init__ (self, implementor, profiles):
        self.implementor = implementor
        self.profiles = profiles
        self.sessions = Sessions()
        # self.implementor.authenticate()

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
        platform = Platform(platform_id, 0, "NO_ENDPOINT", "BUILDING" )
        self.sessions.add_platform(platform)
        try:
           self.implementor.allocate_resources(platform, profile)
        except ResourcesNotAvailable as e:
           return 0
        return platform_id

    def platform_status(self, platform_id):
        """
        The platform status will be BUILDING, CREATED, DESTROYED, FAILED
        platform_id -- the id of the platform
        """
        platform = self.sessions.get_platform(platform_id)
        return self.implementor.allocation_status(platform)

    def get_platform_endpoint(self, platform_id):
        """
        Returns the endpoint.
        platform_id -- the id of the platform
        """
        platform = self.sessions.get_platform(platform_id)
        return platform.get_endpoint()

    def destroy_platform(self, platform_id):
        """
        Destroy the platform.
        platform_id -- the id of the platform
        """
        try :
           platform = self.sessions.get_platform(platform_id)
        except PlatformDoesNotExist as e:
           return 0

        deallocation_status = self.implementor.deallocate_resources(platform)
        return deallocation_status
