#!/usr/bin/python
#-*- coding:utf-8 -*-

from subprocess import Popen, PIPE
import os

class Process(object):
	name = 'Test'

	def __init__(self,name, program, args, workdir):
		self.name = name
		self.program = program
		self.args = args
		self.workdir = workdir

	def _init(self):
		if not os.path.exitsts(self.workdir):
			os.mkdir(self.workdir)
			os.chdir(self.workdir)

	def _pidFile(self):
		return os.path.join(self.workdir, "%s.pid" % self.name)

	def start(self):
		cmd = self.program + '' + self.args
		p = Popen(cmd, stdout=PIPE, shell=True)

	def stop(self):


	def restart(self):
		self.stop()
		self.start()

	def status(self):

	def help(self):
		# print ""

def main():
	name = 'memcached'
	proc = '/usr/bin/memcached'
	args = '-u nobody -p 11211 -c 1024 -m 64'
	wd = '/var/tmp/memcached'
	pm = Process(name = name, program = proc, args = args, workdir = wd)
	try:
		cmd = sys.argv[1]
	except IndexError, e:
		print "Option Error"
		sys.exit()

	if cmd == 'start':
		pm.start()
	elif cmd == 'stop':
		pm.stop()
	elif cmd == 'restart':
		pm.restart()
	elif cmd == 'status':
		pm.status()
	else:
		pm.help()



if __name__ == '__main__':
	main()
