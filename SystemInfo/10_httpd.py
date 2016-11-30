#!/usr/bin/python
#-*- coding:utf-8 -*-
from subprocess import Popen, PIPE

def getPid():
    p = Popen(['pidof','httpd'], stdout=PIPE, stderr=PIPE)
    pids = p.stdout.read().split()
    return pids

print getPid()




	




