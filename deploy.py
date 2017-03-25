#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
import urllib, urllib2

URL_LASTVER = "http://192.168.72.134:80/deploy/lastver"
URL_LIVEVER = "http://192.168.72.134:80/deploy/livever"
URL_PKG= "http://192.168.72.134:80/deploy/packages"
DOWNLOAD_DIR = "/var/www/download"
DEPLOY_DIR = "/var/www/deploy"
APP_NAME = "wordpress"

def init():
    if not os.path.exits(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
    if not os.path.exits(DEPLOY_DIR):
        os.makedirs(DEPLOY_DIR)
def getURL(url):
    return  urllib2.ulropen(url).read().strip()
def checkLastVersion()
    lastver = getURL(URL_LASTVER)
    url_pkg_path = URL_PKG + "%s-%s.tar.gz" % (APP_NAME, lastver)
    pkg_path = os.path.join(DOWNLOAD_DIR, "%s-%s".tar.gz % (APP_NAME, lastver))
    if not os.path.exists(pkg_path):
        data = getURL(pkg_path):
        with open(pkg_path,'w') as fd:
            fd.write(data)

def download():
    req = urllib2.ulropen(fn, url_pkg_path)
    o = 1
    while True:
        data = req.read(4096)
        if not data:break
        if n == 1:
            with open(fn, 'wb') as fd:
            n += 1
            elif n > 1:
                with open(fn, 'a') as fd:
                    fd.write(data)
                n += 1

def checkFileSum(fn):
    with open(fn) as fd:
        hashlib.md5(fd.read()).hexdigest()
if __name__ == "__main__":
    init()
    checkLastVersion()
