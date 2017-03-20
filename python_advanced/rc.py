#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
class Process(object):
    '''memcached rc script'''
    def __init__(self, name, program, args, workdir):
        self.name = name
        self.program = program
        self.args = args
        sele.workdir = workdir

    # Normal Function
    def _init(self):
        pass
    def start(self):
        pass
    def stop(self):
        pass
    def restart(self):
        self.stop()
        self.start()
    def status(self):
        pass

def main():
    try:
        cmd = sys.argv[1]
    except IndexError, e:
        print "Option Error"
        sys.exit()
