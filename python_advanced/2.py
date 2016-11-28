#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys

def isNum(s):
	for i in s:
		if i in '0123456789':
			pass
		else:
			print "%s is not a number" %s
			sys.exit()
	else:
		print "%s is a number" %s
isNum(sys.argv[1])


