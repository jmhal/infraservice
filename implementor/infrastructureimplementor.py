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
        Load credentials. This is totally customized for each infrastructure.
        """
        pass

    def verify_profile_availability(self, profile):
        """
        A large data structure containing all the available resources. The refined
        abstraction will match these to the profiles.
        profile -- the resources needed
        """
        pass

    def allocate_resources(self, platform, profile):
        """
        Allocate the processing nodes on the given infrastructure.
        platform -- the platform that needs the resources
        profile -- the resources needed
        """
        pass

    def allocation_status(self, platform):
        """
        How is the allocation going. This should update the platform object.
        platform -- the platform that needs the resources
        """
        pass

    def deallocate_resources(self, platform):
        """
        Release the allocated machines
        platform -- the platform that was using the resources
        """
        pass
