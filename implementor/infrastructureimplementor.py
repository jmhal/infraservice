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
        Does not return anything.
        """
        pass

    def verify_profile_availability(self, profile):
        """
        Will the allocation of the profile proceed instantaneously?
        profile -- the resources needed
        returns True or False
        """
        pass

    def allocate_resources(self, platform, profile):
        """
        Allocate the processing nodes on the given infrastructure.
        platform -- the platform that needs the resources
        profile -- the resources needed
        Returns the allocation ID
        """
        pass

    def allocation_status(self, platform):
        """
        How is the allocation going. This should update the platform object.
        platform -- the platform that needs the resources
        Returns the Allocation Status
        """
        pass

    def deallocate_resources(self, platform):
        """
        Release the allocated machines
        platform -- the platform that was using the resources
        Does not return anything.
        """
        pass
