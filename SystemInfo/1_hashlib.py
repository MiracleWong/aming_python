#!/usr/bin/python
#-*- coding:utf-8 -*-
import hashlib
import sys

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

if __name__ == '__main__':
	print md5sum(sys.argv[1])




