"""
High Level Operations for every infrastructure
"""
from common.exceptions import ProfileNotFound
from common.sessions import Sessions
import random

class InfrastructureAbstraction:
    def __init__ (self, implementor, profiles):
        self.implementor = implementor
        self.profiles = profiles
        self.sessions = Sessions()

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
        """
        pass

    def create_platform(self, profile_id):
        """
        A platform is a container+infrastructure. This method should allocate
        the resources and deploy the container.
        """
        profile = get_profile(profile_id)
        allocation_id = self.implementor.allocate_resources(profile)
        container_id = self.implementor.deploy_container(allocation_id)
        platform_id = random.randint(0,100000)
        platform = Platform(plataform_id, (allocation_id, container_id), "", "BUILDING" )
        self.sessions.add_platform(platform)
        return platform_id

    def platform_status(self, platform_id):
        """
        BUILDING, READY or DEALLOCATED (for resources and container)?
        """
        platform = self.sessions.get_platform(platform_id)
        allocation_status = self.implementor.allocation_status(platform.get_resources_id()[0])
        deployment_status = self.implementor.container_status(platform.get_resources_id()[0])
        return (allocation_status, deployment_status)

    def destroy_platform(self, plataform_id):
        """
        Destroy the platform.
        """
        pass
