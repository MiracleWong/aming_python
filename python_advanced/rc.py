#!/usr/bin/python
#-*- coding:utf-8 -*-

class Peocess(object):
	name = 'Test'

	def __init__(self,name, program, args, workdir):
		self.name = name
		self.program = program
		self.args = args
		self.workdir = workdir

	def start(self):
		
	def stop(self):
		

	def restart(self):
		self.stop()
		self.start()

	def status(self):
		
def amin():
	try:
		cmd = sys.argv[]
	except IndexError, e:
