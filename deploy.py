#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
import urllib, urllib2
import tarfile
from distutils.version import LooseVersion
import shutil

URL_LASTVER = "http://192.168.72.134:8080/deploy/lastver"
URL_LIVEVER = "http://192.168.72.134:8080/deploy/livever"
URL_PKG= "http://192.168.72.134:80/deploy/packages"
DOWNLOAD_DIR = "/var/www/download"
DEPLOY_DIR = "/var/www/deploy"
APP_NAME = "wordpress"

DOC_ROOT = '/var/www/html/current';


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


def checkLiveVersion():
    livever = getURL(URL_LIVEVER)
    pkg_path = os.path.join(DEPLOY_DIR, "%s-%s" % (APP_NAME, livever))
    if os.path.exists(pkg_path):
        if os.path.exists(DOC_ROOT):
            target = os.readlink(DOC_ROOT)
            if target != pkg_path:
                os.unlink(DOC_ROOT)
                os.symlink(pkg_path, DOC_ROOT)
        else:
            os.symlink(pkg_path, DOC_ROOT)

def versionSort(l):
    from distutils.version import LooseVersion
    vs = [LooseVersion(i) for i in l]
    vs.sort()
    return [i.vstring for i in vs]

def clean():
    download_list = [i.split('-')[1][:-7] for i in os.listdir(DOWNLOAD_DIR)] 
    deploy_list = [i.split('-')[1][:-7] for i in os.listdir(DEPLOY_DIR)] 
    tobe_del_download = versionSort(download_list)[:1]
    tobe_del_deploy = versionSort(deploy_list)[:1]
    for d in tobe_del_download:
        fn = os.path.join(DOWNLOAD_DIR, "%s-%s.tar.gz" % (APP_NAME, d))
        os.remove(fn)
    for d in deploy_list:
        fn = os.path.join(DEPLOY_DIR, "%s-%sz" % (APP_NAME, d))
        shutil.rmtree(fn)

if __name__ == "__main__":
    init()
    checkLastVersion()
    checkLiveVersion()
    clean()