#!/usr/bin/python
#-*- coding:utf-8 -*-
import string
from subprocess import Popen, PIPE

def getIfconfig():
    p = Popen(['ifconfig'], stdout=PIPE)
    data = p.stdout.read().split('\n\n')
    return [i for i in data if i and not i.startswith('lo')]

def paresIfconfig(data):
    re_devname = rc.compile(r'(br|eth|em|virbr|lo|bond)[\d:]+', re.M)
    re_mac = re.compile(r'HWaddr ([0-9A-F:]{17})',re.M)
    re_ip = re.compile(r'inet addr:()[\d\.]{7,15})',re.M)
    devname = re_devname.rearsch(data).group()
    mac = re_mac.rearsch(data).group(1)
    ip = re_ip.findall(data)
    return {devname: [ip, mac]}
if __name__ == '__main__':
    data =  getIfconfig()
    for i in data:
    print paresIfconfig(data)
