#!/usr/bin/python
import socket
import sys
import subprocess
import time

HOST = str(sys.argv[1])
PORT = 5555

proc = subprocess.Popen('hostname', stdout=subprocess.PIPE)
hostname = proc.stdout.read().strip()

proc = subprocess.Popen('cat /proc/cpuinfo | grep processor | wc -l', shell=True, stdout=subprocess.PIPE)
cpu = proc.stdout.read().strip()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

result = 1
while (result != 0):
   result = tcp.connect_ex(dest)
   if (result != 0) :
      print "waiting for server..."
      time.sleep(5)

tcp.send(hostname+ ":" + cpu)
tcp.close()
