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
    def help(self):
        pass 
def main():
    name = 'memcached' 
    prog = '/usr/bin/memcached'
    args = '-u nobody -p 11211 -c 1024 -m 64'
    wd = '/var/tmp/memcached'
    pm = Process(name = name, program = prog, args = args, workdir = wd)
    try:
        cmd = sys.argv[1]
    except IndexError, e:
        print "Option Error"
        sys.exit()
    if cmd == 'start':
        pm.start()
    elif cmd == 'stop':
        pm.stop()
    elif cmd == 'restart':
        pm.restart()
    elif cmd == 'status':
        pm.status()
    else:
        pm.help()

if __name__ == '__main__'
    main()
