"""
High Level Operations for every infrastructure
"""
from common.exceptions import ProfileNotFound
from common.sessions import Sessions

class InfrastructureAbstraction:
    def __init__ (self, implementor, profiles):
        self.implementor = implementor
        self.profiles = profiles
        self.platforms = []

    def get_profile(profile_id):
        for profile in self.profiles.keys():
            if profile_id == self.profiles[profile]['id']
               return profile
        raise ProfileNotFound(profile_id, self.profiles)

    def check_platform_availability(profile_id):
        """
        Not all profiles are readly available.
        For example, a cluster profile may have to wait on queue
        for instantiation. In case of cloud profiles, this method is not used.
        Should it be only on the cluster abstractions?
        """
        pass

    def create_platform(profile_id):
        """
        A platform is a container+infrastructure. This method should allocate
        the resources and deploy the container.
        """
        profile = get_profile(profile_id)
        allocation_id = self.implementor.allocate_resources(profile)
        container_id = self.implementor.deploy_container(allocation_id)
        platform = Platform((allocation_id,container_id), "", "BUILDING" )
        platforms.append(platform)
        return (allocation_id,container_id)

    def platform_status(platform_id):
        """
        Building, ready or deallocated?
        """
        allocation_status = self.implementor.allocation_status(platformid[0])
        deployment_status = self.implementor.container_status(platformid[1])


    def destroy_platform(plataform_id):
        """
        Destroy the platform.
        """
        pass
