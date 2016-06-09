"""
This the cluster abstraction. Here, we see the methods that are commom to all
clusters.
"""
from infrastructureabstraction import InfrastructureAbstraction

class Cluster(InfrastructureAbstraction):
    def __init__(self, clusterImplementor, profiles):
        InfrastructureAbstraction.__init__(self, clusterImplementor, profiles)
