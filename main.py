#!/usr/bin/python
import implementor.slurm

mySlurm = implementor.slurm.Slurm("200.19.177.93", 6080, "pargocad", "/home/jmhal/.ssh/id_dsa.pub")
mySlurm.connect()
mySlurm.squeue("none")
mySlurm.sinfo("node")
mySlurm.close()
