#!/usr/bin/python
#-*- coding:utf-8 -*-

from fabric.api import run
from fabric.api import env

env.user = 'test'
env.password = 'test'

env.hosts = ['localhost', '192.168.1.6']

def host_type():
    check_ver()

def check_ver():
	run("""LIVE_VER=`curl -s http://192.168.72.136:8080/deploy/livever`
    	LIVE_WP=/var/www/deploy/wordpress-$LIVE_VER
    	test -d $LIVE_WP && echo "$LIVE_WP is exists"
    	""")
