#!/usr/bin/python
#-*- coding:utf-8 -*-
import string
import re
from subprocess import Popen, PIPE

def getIfconfig():
    p = Popen(['ifconfig'], stdout=PIPE)
    data = p.stdout.read().split('\n\n')
    return [i for i in data if i and not i.startswith('lo')]

def paresIfconfig(data):
    re_devname = re.compile(r'(br|eth|em|virbr|lo|bond)[\d:]', re.M)
    re_mac = re.compile(r'HWaddr ([0-9A-F:]{17})',re.M)
    re_ip = re.compile(r'inet addr:([\d\.]{7,15})',re.M)
    devname = re_devname.search(data)
    if devname:
        devname = devname.group()
    else:
        devname = ''
    mac = re_mac.search(data)
    if mac:
        mac = mac.group(1)
    else:
        mac = ''
    ip = re_ip.findall(data)
    if ip:
        ip = ip.group(1)
    else:
        ip=''
    return {devname: [ip, mac]}
if __name__ == '__main__':
    data =  getIfconfig()
    dic_ip={}
    for i in data:
        dic_ip.update(paresIfconfig(data))
    for k,v in dic_ip.items():
        print "%-5s: %-15s %s" %(k,v[0],v[1])
