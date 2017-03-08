#!/usr/bin/python
#-*- coding:utf-8 -*-

f = open('/etc/hosts')
while True:
	data = f.readline()
	if not data:
		break
	print data,
f.close()
