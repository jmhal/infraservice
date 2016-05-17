"""
This the cluster abstraction. Here, we see the methods that are commom to all
clusters.
"""
from infrastructureabstraction import InfrastructureAbstraction

class Cluster(InfrastructureAbstraction):
    def __init__(self, clusterImplementor):
        self.__implementor = clusterImplementor

    def allocationList(self):
        pass

    def allocateProfile(self, profile):
        pass

    def allocationStatus(self, allocation):
        pass

    def allocationCancel(self, allocation):
        pass
