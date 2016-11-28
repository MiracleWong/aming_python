#!/usr/bin/python
#-*- coding:utf-8 -*-

def fun():
	sth = raw_input("Please input somthing: ")
	try:
		if type(int(sth)) == type(1):
			print "%s is a number" %sth
	except ValueError:
		print "%s is not a number" %sth

fun()


