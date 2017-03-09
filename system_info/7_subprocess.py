#!/usr/bin/python
#-*- coding:utf-8 -*-
class FuncError(Exception):
	"""docstring for FuncError"""
	def __str__(self):
		return "I am func Error"

def fun():
	raise FuncError()

try:
	# fun()
	print 'a'
except FuncError,e:
	print e
except NameError:
	print '!!'
except Exception:
	print 'Haha'
else:
	print 'Else'
finally:
	print 'Finally'
print "Hello World"


	




