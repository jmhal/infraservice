"""
This is the SLURM cluster implementor. Here we have specific methods that
are equivalent to slurm command line programs.
"""
# This is the implementor class
from infrastructureimplementor import InfrastructureImplementor
from common.platform import Platform

# Import the paramiko module for handling SSH conections.
import paramiko

class Slurm(InfrastructureImplementor):
    def __init__(self, properties):
        """ Set up SSH access.
        In order to execute SLURM commands, this method initializes the IP address
        of the cluster, the user and the ssh key file.
        address -- the IP address of the head node
        port    -- the TCP port for the connection
        user    -- the username
        key     -- filename to the credentials for login
        """
        InfrastructureImplementor.__init__(self, properties)
        self._address = properties['ip']
        self._port = properties['port']
        self._user = properties['user']
        self._key = properties['credentials']
        self._ssh = paramiko.SSHClient()

    def authenticate(self):
        """ Creates a SSH connection
        Will create a connection based on the profile properties.
        """
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh.connect(self._address, self._port, username=self._user, key_filename=self._key)

    def verify_profile_availability(self, profile):
        """
        Use sinfo to see if the queue and the partition has the available resources.
        """
        nodes = int(profile.values()[0]['nodes'])
        partition = profile.values()[0]['partition']
        available_nodes = int(self.sinfo("-p " + partition + " -h --format=%A").split('/')[1])
        if available_nodes >= nodes:
            return True
        else:
            return False

    def allocate_resources(self, platform, profile):
        """
        Use salloc to make an allocation.
        """
        if self.verify_profile_availability(profile) == False:
           return False # I will eventually create an exception here.

        nodes = profile.values()[0]['nodes']
        partition = profile.values()[0]['partition']
        allocation_id = int(self.salloc("-p " + partition + " -n "+ str(nodes) + " --no-shell").split(" ")[4])
        platform.set_allocation_id(allocation_id)
        return allocation_id

    def close(self):
        """ Just closes the SSH connection
        Closes the connection openned in connect()
        """
        self._ssh.close()

    def salloc(self, params):
        """ Allocate resources
        This method will request the resource allocation. It will not guarantee
        instantaneous resouce availability, just return the request ID.
        """
        ssh_stdin, ssh_stdout, ssh_stderr = self._ssh.exec_command("salloc " + params)
        output = ""
        for line in ssh_stderr.readlines():
            output = output + '\n' + line
        return output

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
        ssh_stdin, ssh_stdout, ssh_stderr = self._ssh.exec_command("sinfo " + params)
        output = ""
        for line in ssh_stdout.readlines():
            output = output + '\n' + line
        return output

    def scancel(self, params):
        """ Cancel the allocation
            Destroy the allocation, for any reason
        """
        pass
