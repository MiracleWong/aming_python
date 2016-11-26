#!/usr/bin/python
#-*- coding:utf-8 -*-

# for i in [i**2 for i in range(1,11)]:
# 	print i,

for i in xrange(1,11):
	for j in xrange(1,i+1):
		print "%s x %s = %s" %(j, i, i*j),
	print


