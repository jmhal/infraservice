# This the cluster abstraction. Here, we see the methods that are commom to all
# clusters.
from infrastructureabstraction import InfrastructureAbstraction

class Cloud(InfrastructureAbstraction):
    def __init__(self, cloudImplementor):
        self.__implementor = cloudImplementor;
