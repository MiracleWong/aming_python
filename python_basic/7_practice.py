#!/usr/bin/python
#-*- coding:utf-8 -*-

#猜数字作业
import random
import sys
i=random.randint(1,20)
print i
for s in xrange(6):
    g=raw_input("input you guess number:")
    if g.isdigit():
        g=int(g)
        if g == i:
            print"you win !"
            sys.exit()
        elif g > i:
            print "you number is bigger again %s chance" %(5-s)
        else:
            print "you number is litter again %s chance" %(5-s)
    else:
        print "input a number"
print "you lost!"


