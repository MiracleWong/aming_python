#!/usr/bin/python
#-*- coding:utf-8 -*-

from sys import stdin

data = stdin.read()

chars = len(data)
words = len(data.split())
lines = data.count('\n')

print "%(chars)s %(words)s %(lines)s" %locals()