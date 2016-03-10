import abstraction.InfrastructureAbstraction

class InfrastructureService:
    def __init__(self, file):
        """ Create an instance of the service
        """
        self.load_conf_file(file)

        # Decide what infrastructure to create
        # This is the only section of the service that needs to be update in case
        # of new infrastructures
        if self.infra_type == "cluster":
            if self.cluster_type = "slurm":
                self.infrastructure = InfrastructureAbstraction(Cluster(Slurm()))

        if self.infra_type == "cloud":
            if self.cluster_type = "openstack":
                self.infrastructure = InfrastructureAbstraction(Cloud(Openstack()))

    def load_conf_file(self, file):
        """ Read the configuration file
        Input: config file
        Information necessary from the configuration file:
        - Type of infrastructure (cloud or cluster, openstack or slurm)
        - Profile information
        - Credentials
        Output: OK or error message from unformatted file
        """
        pass

    def allocate(self, profile):
        """ Allocate a profile in the infrastructure
        Input: profile ID
        Output: session ID
        """
        pass

    def session_status(self, session):
        """ Allocation status
        Input: session ID
        Output: status or endpoint
        """
        pass
