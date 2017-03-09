#!/usr/bin/python
# encoding:utf-8

import requests
import urllib2
import re

class MyGS(object):
    """docstring for MyGS"""
    def __init__(self):
        self.headers = {};
        self.baseURL =
        self.loginURL = self.baseURL + '?_task=login'

    def getPage(self):
        self.session = requests.session()
        try:
            response = self.session.get(url = self.baseURL, headers = self.headers)
            return response.text
        except urllib2.URLError, e:
            if  hasattr(e, 'reason'):
                print "连接服务器失败，错误原因", e.reason
                return None

    def getToken(self):
        page = self.getPage()
        re_token = re.compile(r')


        if token:
            pass
        else:
            return None

    def login(self):
        data = {}


        try:
            response = self.session.post(url= self.loginURL, data = data , headers= self.headers, verify = False)
        except urllib2.URLError, e:
            print e

gs = MyGS()
gs.getToken()
gs.login()
