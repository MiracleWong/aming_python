#!/usr/bin/python
#-*- coding:utf-8 -*-

def fabnaci(n):
	if n == 0:
		return 0
	else:
		return n + fabnaci(n-1)

print fabnaci(100)
