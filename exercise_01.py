#!/usr/bin/python
#-*- coding:utf-8 -*-
from optparse import OptionParser
import sys,os

def opt():
    parser = OptionParser()
    parser.add_option("-a","--append",
                      dest="appends",
                      action="store_true",
                      default=False,
                      help="append the strings to file")
    options,args = parser.parse_args()
    return options, args

def input_contents():
    fd = sys.stdin
    data = fd.read()
    return data

def output_contents(options,args,contents):
    outfile = args
    t = 'w'
    print contents,
    if options.appends:
        t = 'a'
    with open(outfile,t) as f:
        sys.stdout = f
        for line in contents:
            sys.stdout.write(line)

def main():
    options,args = opt()
    if len(args) < 1:
        print "%s follow a argument" %__file__
        sys.exit()
    contents = input_contents()
    output_contents(options,args[0],contents)

if __name__ == '__main__':
    main()