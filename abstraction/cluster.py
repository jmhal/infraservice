"""
This the cluster abstraction. Here, we see the methods that are commom to all
clusters.
"""
from infrastructureabstraction import InfrastructureAbstraction

class Cluster(InfrastructureAbstraction):
    def __init__(self, clusterImplementor, profiles):
        InfrastructureImplementor.__init__(self, clusterImplementor, profiles)

    def check_platform_availability(profile_id):
        """
        This is a cluster. So we need to check the queue.
        """
        profile = self.get_profile(profile_id)
        return self.implementor. 


    def create_platform(profile_id):
        """
        This is a cluster. So we need to submit the allocation to the queue.
        """
        pass

    def platform_status(platform_id):
        """
        This is a cluster. How is our allocation at the queue?
        """
        pass

    def destroy_platform(plataform_id):
        """
        This a cluster. Cancel the allocation.
        """
        pass
