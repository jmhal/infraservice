from common.sessions import Sessions
# Primitive Operations
class InfrastructureImplementor:
    """
    This is the abstract class for the implementor.
    """
    def __init__(self, properties):
        self.properties = properties

    def authenticate(self):
        """
        Load credentials
        """
        pass

    def verify_profile_availability(self, profile):
        """
        A large data structure containing all the available resources. The refined
        abstraction will match these to the profiles.
        """
        pass

    def allocate_resources(self, platform, profile):
        """
        Allocate the processing nodes on the given infrastructure. This will have
        to start a thread to update the platform status.
        """
        pass

    def allocation_status(self, allocation_id):
        """
        How is the allocation going.
        """
        pass

    def deallocate_resources(self, platform):
        """
        Release the allocated machines
        """
        pass

    def deploy_container(self, allocation_id):
        """
        Deploy the component container.
        """
        pass

    def container_status(self, allocation_id):
        """
        Returns the status of the container.
        """
        pass

    def get_container_endpoints(self, allocation_id):
        """
        Retrieve the container's endpoint for componente deployment.
        """
        pass

    def destroy_container(self, container_id):
        """
        Destroy the container.
        """
        pass
