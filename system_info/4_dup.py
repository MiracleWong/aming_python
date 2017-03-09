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

def gen_dic(topdir):
	dic = {}
	a = os.walk(topdir)
	for p,d,f in a:
		for i in f:
			fn = os.path.join(p,i)
			md5 = md5sum(fn)
			if dic.has_key(md5):
				dic[md5].append(fn)
			else:
				dic[md5] = [fn]
	return dic

if __name__ == '__main__':
	dic = gen_dic(sys.argv[1])
	for k, v in dic.items():
		if len(v) > 1:
			print k, v
	




