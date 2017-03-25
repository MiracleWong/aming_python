#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
import urllib, urllib2

URL_LASTVER = "http://192.168.72.134/deploy/lastver"
URL_LIVEVER = "http://192.168.72.134/deploy/livever"
URL_PKG= "http://192.168.72.134/deploy/packages"
DOWNLOAD_DIR = "/var/www/download"
DEPLOY_DIR = "/var/www/deploy"
APP_NAME = "wordpress"

def init():
    if not os.path.exits(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
    if not os.path.exits(DEPLOY_DIR):
        os.makedirs(DEPLOY_DIR)

def checkLastVersion():
    urllib2.ulropen(DOWNLOAD_DIR)


if __name__ == "__main__":
    init()
