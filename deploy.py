#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
import urllib, urllib2
import tarfile

URL_LASTVER = "http://192.168.72.134:8080/deploy/lastver"
URL_LIVEVER = "http://192.168.72.134:8080/deploy/livever"
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
    return urllib2.ulropen(url).read().strip()
def checkLastVersion()
    lastver = getURL(URL_LASTVER)
    url_pkg_path = URL_PKG + "%s-%s.tar.gz" % (APP_NAME, lastver)
    pkg_path = os.path.join(DOWNLOAD_DIR, "%s-%s".tar.gz % (APP_NAME, lastver))
    if not os.path.exists(pkg_path):
        if not download(pkg_path, url_pkg_path):
            return False
        print "SUCCESS"
    extract_dir = os.path.join(DEPLOY_DIR, "%s-%s" % (APP_NAME, lastver))
    if not os.path.exists(extract_dir):
        pkg_deploy(pkg_path, DEPLOY_DIR)

def download(fn, url_pkg_path):
    url_pkg_path_md5 = url_pkg_path +'.md5'

    req = urllib2.ulropen(fn, url_pkg_path)
    n = 1
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
    if checkFileSum(fn, md5f):
        return True
    return False

def checkFileSum(fn, md5):
    with open(fn) as fd:
        m = hashlib.md5(fd.read()).hexdigest()
        if m == md5:
            return True
        return False

def pkg_deploy(fn, d):
    tar = tarfile.open(fn)
    tar.extractall(path=d)

if __name__ == "__main__":
    init()
    checkLastVersion()
