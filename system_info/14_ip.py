#!/usr/bin/python
#-*- coding:utf-8 -*-

import string
from subprocess import Popen, PIPE

def getIP1():
    p = Popen(['ifconfig'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    data =  [i for i in stdout.split('\n') if i and not i.startswith('lo')]
    return data

def getIP(data):
	new_line = ''
	lines = []
	for line in data:
		if line[0].strip():
			lines.append(line)
			new_line = line + '\n'
		else:
			new_line += line + '\n'
	lines.append(new_line)
	return [i for i in lines if i and not i.startswith('lo')]

def paresIfconfig(data):
	dic = {}
	for lines in data:
		line_list = lines.split('\n')
		devname = line_list[0].split()[0]
		macaddr = line_list[0].split()[-1]
		ipaddr = line_list[1].split()[1].split(':')[1]
		dic[devname] = [ipaddr, macaddr]
	return dic

if __name__ == '__main__':
	data = getIP1()
	print getIP(data)
