#!/usr/bin/python
# encoding:utf-8


import urllib, urllib2
import re

def getHrml(url):
	page = urllib2.urlopen(url)
	return page.read()


def getImage(html):
	re_img = re.compile(r'<img class="BDE_Image" src="(.*?)".*?>')
	img_list = re_img.findall(html)
	i = 1
	for imgurl in img_list:
		print imgurl
		urllib.urlretrieve(imgurl, filename="%s.jpg" %i)
		i += 1

if __name__ == '__main__':
	url = 'http://tieba.baidu.com/p/4229162765';
	page = getHrml(url)
	img = getImage(page)
