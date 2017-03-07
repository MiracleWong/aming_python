#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys,os

def isNum(s):
	if s.isdigit():
		return True
	else:
		return False

for i in os.listdir('/proc'):
	if isNum(i)
		print i
