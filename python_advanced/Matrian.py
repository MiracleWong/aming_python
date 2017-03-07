#!/usr/bin/python
#-*- coding:utf-8 -*-

class People(object):
	"""docstring for People"""
	color = 'yellow'

	## 多重继承的时候，最先选择继承最早的类的构造函数
	def __init__(self):
		print "Init..."
		self.dwell = 'Earth'
		self.color = 'yellow'

	def think(self):
		print "I am as %s" % self.color
		print "I home is on %s" % self.dwell

class Martian(object):
	"""docstring for Martian"""
	color = 'red'
	def __init__(self):
		self.dwell = 'Martian'


class Chinese(Martian, People):
	"""docstring for Chinese"""
	def __init__(self):
		# super(Chinese, self).__init__('red')
		People.__init__(self)

	def talk(self):
		print "I like talking"
my = Chinese()
my.think()
