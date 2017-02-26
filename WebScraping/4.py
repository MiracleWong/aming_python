#!/usr/bin/python
# encoding:utf-8

import sys
import urllib, urllib2
import re

dic = {'hostname': 'n2', 'ip': '2.2.2.2'}

# url = 'http://127.0.0.1:8000/db/' + '?' + urllib.urlencode(dic)
url = 'http://127.0.0.1:8000/db/'


response = urllib2.urlopen(url, urllib.urlencode(dict))
print response.read()
