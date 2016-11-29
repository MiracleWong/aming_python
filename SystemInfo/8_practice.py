#!/usr/bin/python
#-*- coding:utf-8 -*-
import os,sys
from subprocess import Popen,PIPE

class FuncError(Exception):
    def __str__(self):
        return 'FuncError'
def fun():
    raise FuncError()

def readFile():
    file=sys.argv[1]
    if os.path.exists(file):
        if os.path.isdir(file):
            print '%s is a dir'%file
            sys.exit()
        if os.path.isfile(file):
           p=Popen(['cat',file],stdout=PIPE)
           data=p.stdout.read()
           return data
        else:
            try:
                raise FuncError()
            except FuncError,e:
                print e
                sys.exit()
    else:
        print '%s is not exist' %file
        sys.exit()
if __name__=='__main__':
    try:
        print readFile()
    except IndexError:
        print 'please follow the argv and write correctly'




	




