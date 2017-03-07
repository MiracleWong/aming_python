#!/usr/bin/python
#-*- coding:utf-8 -*-

class MyClass(object):
	var1 = '类属性，类的公有属性 var1'
	__var2 = '类属性，类的私有有属性 var2'

	def func1(self):
		self.var3 = '对象的公有属性 var3'
		self.__var4 = '对象的私有属性 var4'
		var5 = '函数的局部变量'
		print self.__var4
		print var5

	def func2(self):
		print self.var1
		print self.__var2
		print self.var3
		print self.__var4

mc = MyClass()
# print mc.var1
# print mc._MyClass__var2

mc.func1()			# 如果没有使用方法，则无法访问其中的属性
# print mc.var3
# print mc._MyClass__var4
print '*'*25
mc.func2()
print '*'*25

print mc.__dict__  ## 内置属性，就是var4和var3
print '*'*25
print MyClass.__dict__
