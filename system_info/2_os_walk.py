#!/usr/bin/python
#-*- coding:utf-8 -*-
import hashlib
import sys, os

def md5sum(f):
	m = hashlib.md5()
	with open(f) as fd:
		while True:
			data = fd.read(4096)
			if data:
				m.update(data)
			else:
				break
	return m.hexdigest()

s = ''
a = os.walk(sys.argv[1])
for p,d,f in a:
	for i in f:
		fn = os.path.join(p,i)
		md5 = md5sum(fn)
		s += md5 + ' ' + fn + '\n'

print s,
	




