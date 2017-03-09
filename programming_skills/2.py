#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys

def lineCount(fd):
	n = 0
	for i in fd.readlines():
		n += 1
	return n
input = sys.stdin
print lineCount(input)