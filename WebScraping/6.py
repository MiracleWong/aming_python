#!/usr/bin/python
# encoding:utf-8

import requests
import urllib2
import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
session = requests.session()
params = {
"language":"-1",
"style":"-1",
"df":"mail126_letter",
"from":"web",
"allssl":"false",
"race":"-2_-2_-2_db",
"net":"failed",
"iframe":"1",
"savelogin": "1",
"passtype": "0",
"product":"mail126",
"url2":"http://mail.126.com/errorpage/error126.htm",
"funcid": "loginone",
}
data = {
    "username":"cfwr1991@126.com",
    "password":"CFwr9118@123"
}
url = "https://mail.126.com/entry/cgi/ntesdoor?"

login = session.post(url = url, data = data, headers = headers, params = params)
print login.url
print login.status_code
print login.text

re_url = re.compile(r'href = "(.*?)"')
url = re_url.findall(login.text)[0]
print url
