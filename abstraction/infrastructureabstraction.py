"""
High Level Operations for every infrastructure
"""
from common.exceptions import ProfileNotFound
from common.sessions import Sessions
import uuid

class InfrastructureAbstraction:
    def __init__ (self, implementor, profiles):
        self.implementor = implementor
        self.profiles = profiles
        self.sessions = Sessions()
        self.implementor.authenticate()

    def get_profile(profile_id):
        for profile in self.profiles.keys():
            if profile_id == self.profiles[profile]['id']
               return profile
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
        profile = get_profile(profile_id)
        available =  self.implementor.verify_profile_availability(profile)
        return available

    def create_platform(self, profile_id):
        """
        A platform is a container+infrastructure. This method should allocate
        the resources and deploy the container.
        profile_id -- the desired profile.
        """
        profile = get_profile(profile_id)
        platform_id = uuid.uuid4()
        platform = Platform(plataform_id, 0, "NO_ENDPOINT", "BUILDING" )
        self.sessions.add_platform(platform)
        self.implementor.allocate_resources(platform, profile)
        return platform_id

    def platform_status(self, platform_id):
        """
        The platform status will be BUILDING, CREATED, DESTROYED, FAILED 
        platform_id -- the id of the platform
        """
        platform = self.sessions.get_platform(platform_id)
        return platform.get_status()

    def get_platform_endpoint(self, platform_id):
        """
        Returns the endpoint.
        platform_id -- the id of the platform
        """
        platform = self.sessions.get_platform(platform_id)
        platform.get_endpoint()

    def destroy_platform(self, plataform_id):
        """
        Destroy the platform.
        platform_id -- the id of the platform
        """
        platform = self.sessions.get_platform(platform_id)
        deallocation_status = self.implementor.deallocate_resources(platform)
        return deallocation_status
