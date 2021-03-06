"""
This is the SLURM cluster implementor. Here we have specific methods that
are equivalent to slurm command line programs.
"""
# This is the implementor class
from infrastructureimplementor import InfrastructureImplementor
from common.platform import Platform
from common.exceptions import ResourcesNotAvailable

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

        self.results_status = {
           'PENDING': "BUILDING",
           'COMPLETING': "BUILDING",
           'CONFIGURING': "BUILDING",
           'RUNNING':"CREATED",
           'COMPLETED': "DESTROYED",
           'SUSPENDED': "FAILED",
           'CANCELLED': "FAILED",
           'FAILED': "FAILED",
           'TIMEOUT': "FAILED",
           'PREEMPTED': "FAILED",
           'NODE_FAIL': "FAILED"
        }

    def authenticate(self):
        """ Creates a SSH connection
        Will create a connection based on the profile properties.
        Does not return anything.
        """
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh.connect(self._address, self._port, username=self._user, key_filename=self._key)

    def verify_profile_availability(self, profile):
        """
        Use sinfo to see if the queue and the partition has the available resources.
        profile -- the dictionary with the profile data.
        returns True or False
        """
        nodes = profile['nodes']
        partition = profile['partition']
        available_nodes = int(self.sinfo("-p " + partition + " -h --format=%A").split('/')[1])

        if available_nodes >= nodes:
            return True
        else:
            return False

    def allocate_resources(self, platform, profile):
        """
        Use salloc to make an allocation.
        platform -- the object to be updated with the allocation id
        profile -- the dictionary with the profile data.
        Returns the allocation ID
        """
        profile_id = profile['id']
        nodes = profile['nodes']
        partition = profile['partition']

        if self.verify_profile_availability(profile) == False:
            raise ResourcesNotAvailable(profile_id, partition + ":" + str(nodes))

        allocation_id = int(self.salloc("-p " + partition + " -n "+ str(nodes) + " --no-shell").split(" ")[4])
        platform.set_allocation_id(allocation_id)

        platform.set_status("BUILDING")
        return allocation_id

    def allocation_status(self, platform):
        """
        How is the allocation going. May be one of the following:
        PENDING, RUNNING, SUSPENDED, CANCELLED, COMPLETING,
        COMPLETED, CONFIGURING, FAILED, TIMEOUT, PREEMPTED, and NODE_FAIL
        See the man page of squeue for details.
        platform -- the platform that needs the resources
        Returns the Allocation Status
        """
        slurm_status = self.squeue("-h -j " + str(platform.get_allocation_id()) + " -o %T")[:-1]
        platform_status = self.results_status[slurm_status]
        platform.set_status(platform_status)
        return platform.get_status()

    def deallocate_resources(self, platform):
        """
        Release the allocated machines
        platform -- the platform that was using the resources
        Does not return anything.
        """
        allocation_id = platform.get_allocation_id()
        self.scancel(str(allocation_id))
        platform.set_status("DESTROYED")
        return True

    def close(self):
        """ Just closes the SSH connection
        Closes the connection openned in self.authenticate()
        """
        self._ssh.close()

    def salloc(self, params):
        """ Allocate resources
        This method will request the resource allocation. It will not guarantee
        instantaneous resouce availability, just return the request ID.
        params -- the parameters to the command
        """
        self.authenticate()

        ssh_stdin, ssh_stdout, ssh_stderr = self._ssh.exec_command("salloc " + params)
        output = ""
        for line in ssh_stderr.readlines():
            output = output + line

        self.close()
        return output

    def squeue(self, params):
        """ Verify the allocation status
        This will see the position of the allocation on the queue
        params -- the parameters to the command
        """
        self.authenticate()

        ssh_stdin, ssh_stdout, ssh_stderr = self._ssh.exec_command("squeue " + params)
        output = ""
        for line in ssh_stdout.readlines():
            output = output + line

        self.close()
        return output

    def sinfo(self, params):
        """ Verify the cluster status
        This will return information about the status of the cluster, the number
        of idle and allocated machines.
        params -- the parameters to the command
        """
        self.authenticate()

        ssh_stdin, ssh_stdout, ssh_stderr = self._ssh.exec_command("sinfo " + params)
        output = ""
        for line in ssh_stdout.readlines():
            output = output + line

        self.close()
        return output

    def scancel(self, params):
        """ Cancel the allocation
        Destroy the allocation, for any reason
        params -- the parameters to the command
        """
        self.authenticate()

        ssh_stdin, ssh_stdout, ssh_stderr = self._ssh.exec_command("scancel " + params)
        output = ""
        for line in ssh_stdout.readlines():
            output = output + line

        self.close()
        return output

def main():
   properties = {
      'user': 'jmhal',
      'credentials': "/home/jmhal/.ssh/id_rsa.pub",
      'ip': "192.168.0.11",
      'port': 22
   }

   profile = {
      'earth': {
         'id': 0,
         'partition': "long",
         'nodes': 1,
      }
   }

   earth = Slurm(properties)
   earth.authenticate()

   p = Platform(0, 0, "", "BUILDING")
   print "Initial Platform: "
   print p
   if earth.verify_profile_availability(profile):
       allocation_id = earth.allocate_resources(p, profile)
       p.set_allocation_id(allocation_id)
       print "After Allocation "
       print p
       print earth.allocation_status(p)
       print "After Status Update "
       print p
       earth.deallocate_resources(p)
       print "After Deallocation "
       print p
   else:
       print "Insuffiecient Resources..."

if __name__ == "__main__":
   main()
