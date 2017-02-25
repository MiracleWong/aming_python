#!/usr/bin/python
# encoding:utf-8


import urllib, urllib2
import re


page = 1
url = 'http://www.qiushibaike.com/8hr/page/' + str(page);
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
try:
	request = urllib2.Request(url,headers = headers)
	response = urllib2.urlopen(request)
	print response.read()
except urllib2.URLError, e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e, "reason"):
		print e.code
