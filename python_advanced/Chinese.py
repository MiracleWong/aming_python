#!/usr/bin/python
#-*- coding:utf-8 -*-

class People(object):
	"""docstring for People"""
	color = 'yellow'

	def __init__(self, c):
		print "Init..."
		self.dwell = 'Earth'


	def think(self):
		print "I am as %s" % self.color
		print "I am a thinker"

	def __talk(self):
		print "I am talking with Tom"

class Chinese(People):
	"""docstring for Chinese"""
	def __init__(self):
		# super(Chinese, self).__init__('red')
		People.__init__(self,'red')

	def talk(self):
		print "I like talking"
my = Chinese()
print my.color
my.think()
my.talk()
