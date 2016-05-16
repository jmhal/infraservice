# High Level Operations
class InfrastructureAbstraction:
    def __init__ (self, implementor):
        self.__implementor = implementor

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
        the infrastructure and deploy the container.
        """
        pass

    def platform_status(platform_id):
        """
        Building, ready or deallocated?
        """
        pass

    def destroy_platform(plataform_id):
        """
        Destroy the platform.
        """
        pass
