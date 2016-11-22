#!/usr/bin/python
#-*- coding:utf-8 -*-

with open('/etc/hosts') as fd:
	while  True:
		data = fd.readline()
		if not data:
			break
		print data