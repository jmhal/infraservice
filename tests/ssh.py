#!/usr/bin/python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("200.19.177.93", 6080, username="pargocad", password="#liaufcbr$7322")
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("uptime")

for line in ssh_stdout.readlines():
    print line
