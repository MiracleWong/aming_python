#!/usr/bin/python
#-*- coding:utf-8 -*-

class People(object):
	"""docstring for People"""
	color = 'yellow'
	__age = 30

	class Chinese(object):
		"""docstring for Chinese"""
		name = "I am Chinese"


	def __str__(self):
		return "This is People class"

	def __init__(self):
		pass

	def __init__(self, c = 'white'):
		self.color = c


	def think(self):
		self.color = 'black'
		print "I am as %s" % self.color
		print "I am a thinker"
		print self.__age

	def __talk(self):
		print "I am talking with Tom"

	@classmethod
	def test(self):
		print "This is class method"
		print People.color

	@staticmethod
	def test1():
		print "This is static method"
		print People.__age


	## destructor
	def __del__(self):
		print "Del..."
		self.fd.close()


jack = People()
People.test()
People.test1()
print jack
tom = People.Chinese()
print tom.name
print People.Chinese.name
print People.Chinese().name

## 1
my = People('Green')
print my.color
print People.color
