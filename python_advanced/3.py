#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys,os

def isNum(s):
	for i in s:
		if i in '0123456789':
			pass
		else:
			print "%s is not a number" %s
			break
		print "%s is a number" %s

for i in os.listdir('/proc'):
	isNum(i)


