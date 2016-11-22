#!/usr/bin/python
# encoding:utf-8

class People(object):
	"""docstring for People"""
	color = 'yellow'
	__age = 30

	class Chinese(object):
		"""docstring for Chinese"""
		name = 'Miracle Wong'
		# print "I am Chinese"			

	def think(self):
		self.color = "black"
		print "I am a %s" % self.color
		print "I am a thinker"
		# print self.__age

ren = People()
ren.color = '白色人'
print ren.color
ren.think()
# print ren._People__age		# test
print ren.__dict__
print "#" *30
print People.color
print People.__dict__

print People.Chinese().name
		              