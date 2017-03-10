#!/usr/bin/python
#-*- coding:utf-8 -*-

import string
from subprocess import Popen, PIPE


p=Popen(['dmidecode'], stdout=PIPE)
data=p.stdout
lines = []
dmi = {}
a = True
while a:
	line = data.readline()
	if line.startswith('System Information'):
		while True:
			line = data.readline()
			if line == '\n':
				a = False
				break
			else:
				lines.append(line)
dmi_dic = dict([i.strip().split(':') for i in lines])
for k, v in dmi_dic.items():
	dmi[k] = v.strip()
print dmi

	




	




