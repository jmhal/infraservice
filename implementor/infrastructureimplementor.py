# Primitive Operations
class InfrastructureImplementor:
    """
    This is the abstract class for the implementor.
    """
    def __init__(self, properties):
        self.properties = properties
        pass

    def authenticate(self):
        """
        Will process the credentials and set up the variables for authentication.
        """
        pass

    def verify_profile_availability(self, profile):
        """
        A large data structure containing all the available resources. The refined
        abstraction will match these to the profiles.
        """
        pass

    def allocate_resources():
        """
        Allocate the processing nodes on the given infrastructure.
        """
        pass

    def allocation_status():
        """
        How is the allocation going.
        """
        pass

    def deallocate_resources():
        """
        Release the allocated machines
        """
        pass

    def deploy_container():
        """
        Deploy the component container.
        """
        pass

    def container_status():
        """
        Returns the status of the container.
        """
        pass

    def get_container_endpoints():
        """
        Retrieve the container's endpoint for componente deployment.
        """
        pass

    def destroy_container():
        """
        Destroy the container.
        """
        pass

x
