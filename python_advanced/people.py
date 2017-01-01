#!/usr/bin/python
#-*- coding:utf-8 -*-

class People(object):
	"""docstring for People"""
	color = 'yellow'
	__age = 30

	def think(self):
		self.color = 'black'
		print "I am as %s" % self.color
		print "I am a thinker"
		print self.__age

	def __talk(self):
		print "I am talking with Tom"

	@classmethod
	def test(self):
		print People.color

	@staticmethod
	def test1():
		print People.__age


jack = People()
People.test()
People.test1()
		


