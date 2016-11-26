#!/usr/bin/python
#-*- coding:utf-8 -*-
info = {}
name = raw_input("Please input name: ")
age = raw_input("Please input age: ")
gender = raw_input("Please input (M/F): ")

info['name'] = name
info['age'] = age
info['gender'] = gender

# 缩进的时候，尽可能的使用4个空格，而不是Tab键
# 4个规格已经形成了业界的编程规范
for k,v in info.items():
	print "%s : %s" % (k, v)





