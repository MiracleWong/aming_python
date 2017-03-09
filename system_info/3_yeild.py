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

def file_md5(topdir):
	a = os.walk(topdir)
	for p,d,f in a:
		for i in f:
			fn = os.path.join(p,i)
			md5 = md5sum(fn)
			yield "%s %s" % (md5 , fn)
if __name__ == '__main__':
	try:
		topdir = sys.argv[1]
	except IndexError:
		print "%s follow a dir"
		sys.exit()
	gen = file_md5(topdir)
	for i in gen:
		print i
	




