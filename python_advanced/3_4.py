#!/usr/bin/python
#-*- coding:utf-8 -*-

class MyClass(object):
	name = 'Test'

	def __init__(self):
		self.func1()
		self.__func2()

	def func1(self):
		print self.name
		print "我是公有方法"
		# self.__func2()
	def __func2(self):
		print self.name
		print "我是私有方法"

	@classmethod
	def classFunc(self):
		print self.name
		print "我是类方法"
	@staticmethod
	def staticFunc():
		print MyClass.name
		print "我是静态方法"

mc = MyClass()
# mc.func1()
#
# MyClass.classFunc()
# MyClass.staticFunc()
mc.__init__
