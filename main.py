#!/usr/bin/python
import implementor.slurm

mySlurm = implementor.slurm.Slurm("XXX.XXX.XXX.XXX", 6080, "XXXX", "/home/XXXX/.ssh/id_dsa.pub")
mySlurm.connect()
mySlurm.squeue("none")
mySlurm.sinfo("node")
mySlurm.close()
