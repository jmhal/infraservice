# Primitive Operations
class InfrastructureImplementor:
    """
    This is the abstract class for the implementor.
    """
    def __init__(self, profiles):
        self.profiles = profiles
        pass

    def allocate_machines():
        """
        Allocate the processing nodes on the given infrastructure
        """
        pass

    def deploy_container():
        """
        Deploy the component container
        """
        pass

    def status():
        """
        Returns the status
        """
        pass

    def get_container_endpoints():
        """
        Retrieve the container's endpoint for componente deployment
        """
        pass

    def deallocate_machines():
        """
        Release the allocated machines
        """
        pass
