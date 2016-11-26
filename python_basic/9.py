#!/usr/bin/python
#-*- coding:utf-8 -*-

# for i in [i**2 for i in range(1,11)]:
# 	print i,

with open('tmp.txt') as fd:
	while True:
		line = fd.readline()
		if not line:
			break
		print line,


