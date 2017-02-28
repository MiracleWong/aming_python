#!/usr/bin/python
# encoding:utf-8


import urllib, urllib2
import re
from bs4 import beautifulSoup


# page = 2
# url = 'http://www.qiushibaike.com/8hr/page/' + str(page);
url = "http://mp.weixin.qq.com/s/OrrT2RZ4J50Z22n1QYYyJw";
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
try:
	request = urllib2.Request(url,headers = headers)
	response = urllib2.urlopen(request)
	html = response.read()
	print html
except urllib2.URLError, e:
	if hasattr(e,"code"):
		print "连接服务器失败，错误代码：%s" %e.code
	if hasattr(e, "reason"):
		print "连接服务器失败，错误原因：%s" %e.reason
#
# re_page = re.compile(r'<div class="author.*?>.*?<a.*?<img.*?alt="(.*?)"/>.*?<div class="content">(.*?)</div>.*?<div class="stats">.*?<i class="number">(\d+)</i>', re.S)
#
# items = re_page.findall(html)
# for item in items:
# 	for i in item:
# 		print i
