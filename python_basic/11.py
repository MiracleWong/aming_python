#!/usr/bin/python
#-*- coding:utf-8 -*-

# 计算计算机的mac地址
macaddr = 'ac:bc:32:d6:37:b5'
prefix_mac = macaddr[:-3]
last_two = macaddr[-2:]
plus_one = int(last_two, 16) + 1
if plus_one in range(10):
	new_last_two = hex(plus_one)[2:]
	new_last_two = '0' + new_last_two
else:
	new_last_two = hex(plus_one)[2:]
	if len(new_last_two) == 1:
		new_last_two = '0' + new_last_two

new_mac = prefix_mac + ':' + new_last_two
print new_mac.upper()


