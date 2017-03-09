#!/usr/bin/python
#-*- coding:utf-8 -*-
import os,sys, string

def isNum(s):
	for i in s:
		if i in string.digits:
			continue
		else:
			return False
	return True


for pid in os.listdir('/proc'):
	# if pid.isdiigt():
	if isNum(pid):
		print pid

	




