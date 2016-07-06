#!/usr/bin/python

import socket
import threading
import sys

count = int(sys.argv[1])
HOST = ''
PORT = 5555

def connection(con, client):
   hostnamecpu = con.recv(1024)
   hostname = hostnamecpu.strip().split(':')[0]
   cpu = hostnamecpu.strip().split(':')[1]

   ip = client[0].strip()

   # /etc/hosts
   f = open("hosts","a")
   f.write(ip + " " + hostname + "\n")
   f.close()
 
   # /etc/openmpi/openmpi-default-hostfile
   f = open("machinefile","a")
   f.write(ip + " slots=" + cpu + "\n")
   f.close()

   con.close()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

for i in range(count):
   con, client = tcp.accept()
   #thread.start_new_thread(connection, tuple([con, client]))
   t = threading.Thread(target=connection, args=(con, client))
   t.start()

t.join()
tcp.close()

