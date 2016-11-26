#!/usr/bin/python
#-*- coding:utf-8 -*-

with open('/proc/meminfo') as fd:
	for line in fd:
		if line.startswith('memTotal'):
			total = line.split()[1]
			continue
		if line.startswith('MemFree'):
			free = line.split()[1]
			break

print "%.2f" %(int(free)/1024.0)+'M'


