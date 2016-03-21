#!/usr/bin/python
import paramiko

ssh = paramiko.SSHClient()

# The server must be configured to use only rsa or dsa, not ecdsa
# This configuration is available at /etc/ssh/sshd_config
ssh.load_system_host_keys()

# The alternative is to accept whatever key the server sends
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("200.19.177.93", 6080, username="pargocad", key_filename="/home/jmhal/.ssh/id_dsa.pub")

# Connect with password
ssh.connect("200.19.177.93", 6080, username="pargocad", password="#liaufcbr$7322")

ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("uptime")

for line in ssh_stdout.readlines():
    print line

ssh.close()
