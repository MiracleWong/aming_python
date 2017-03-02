#!/usr/bin/python
#-*- coding:utf-8 -*-
class Process(object):
    '''rc script'''
    def __init(self, name, program, args,workdir)
        self.name = name
        self.program = program
        self.args = args
        self.workdir = workdir

    def start(self):
    def stop(self):
    def restart(self):
    def status(self):


def main():
    try:
        cmd = sys.argv[1]
    except IndexError, e:
        print "Option E"
