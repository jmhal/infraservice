# This is the SLURM cluster implementor. Here we have specific methods that
# are equivalent to slurm command line programs.

# This is the implementor class
from infrastructureimplementor import InfrastructureImplementor

# Import the paramiko module for handling SSH conections.
import paramiko

class Slurm(InfrastructureImplementor):
    def __init__(self, address, port, user, key):
        """ Set up SSH access
        In order to execute SLURM commands, this method initializes the IP address
        of the cluster, the user and the ssh key file.
        """
        self._address = address
        self._port = port
        self._user = user
        self._key = key

        self._ssh = paramiko.SSHClient()
        self._ssh.load_system_host_keys()

    def connect(self):
        """ Creates a SSH connection
        Will create a connection based on the constructor parameters.
        """
        self._ssh.connect(self._address, self._port, username=self._user, key_filename=self._key)

    def close(self):
        """ Just closes the SSH connection
        Closes the connection openned in connect()
        """
        self._ssh.close()

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
        ssh_stdin, ssh_stdout, ssh_stderr = self._ssh.exec_command("salloc")
        for line in ssh_stdout.readlines():
            print line

    def squeue(self, params):
        """ Verify the allocation status
        This will see the position of the allocation on the queue
        """
        ssh_stdin, ssh_stdout, ssh_stderr = self._ssh.exec_command("squeue -h")
        for line in ssh_stdout.readlines():
            print line

    def sinfo(self, params):
        """ Verify the cluster status
        This will return information about the status of the cluster, the number
        of idle and allocated machines.
        """
        ssh_stdin, ssh_stdout, ssh_stderr = self._ssh.exec_command("sinfo -h")
        for line in ssh_stdout.readlines():
            print line

    def scancel(self, params):
        """ Cancel the allocation
            Destroy the allocation, for any reason
        """
        pass
