# This is the SLURM cluster implementor. Here we have specific methods that
# are equivalent to slurm command line programs.
class Slurm(InfrastructureImplementor):
    def __init__(self, address, user, key):
        """ Set up SSH access
        In order to execute SLURM commands, this method initializes the IP address
        of the cluster, the user and the ssh key file.
        """
        self._address = address
        self._user = user
        self._key = key

    def parseprofile(self, profile):
        """ Parse profile to params
        Receive the profile description and turn it into params for salloc
        """
        pass

    def salloc(self, params):
        """ Allocate resources
        This method will request the resource allocation. It will not guarantee
        instantaneous resouce availability, just return the request ID.
        """
        pass

    def squeue(self, params):
        """ Verify the allocation status
        This will see the position of the allocation on the queue
        """
        pass

    def sinfo(self, params):
        """ Verify the cluster status
        This will return information about the status of the cluster, the number
        of idle and allocated machines.
        """
        pass

    def scancel(self, params):
        """ Cancel the allocation
            Destroy the allocation, for any reason
        """
        pass
