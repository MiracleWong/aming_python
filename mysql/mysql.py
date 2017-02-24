#!/usr/bin/python
#-*- coding:utf-8 -*-

from ConfigParser import ConfigParser

class MySQLDConfig(ConfigParser):
	"""docstring for MySQLDConfig"""
	def __init__(self, config):
		ConfigParser.__init__(self, allow_no_value=True)
		self.config = config
		self.read(self.config)

if __name__ == '__main__':
	mc = MySQLDConfig('/usr/local/mysql/support-files/my-default.cnf')
	print mc.get('mysqld', 'user')
