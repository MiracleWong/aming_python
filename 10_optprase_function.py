#!/usr/bin/python
#-*- coding:utf-8 -*-
from optparse import OptionParser
import sys, os

def opt():
	parser = OptionParser()
	parser.add_option("-c", "--char",
		dest="chars",
		action="store_true",
		default=False,
		help="only count chars")
	parser.add_option("-w", "--word",
		dest="words",
		action="store_true",
		default=False,
		help="only count words")
	parser.add_option("-l", "--line",
		dest="lines",
		action="store_true",
		default=False,
		help="only count lines")
	options, args = parser.parse_args()
	return options, args

def get_count(data):
	chars = len(data)
	words = len(data.split())
	lines = data.count('\n')
	return lines, words, chars

def print_wc(fn, options, lines, words, chars):
	if options.lines:
		print lines,
	if options.words:
		print words,
	if options.chars:
		print chars,
	print fn

def main():
	options, args = opt()
	if not (options.lines or options.words or options.lines):
		options.lines, options.words, options.chars = True, True, True
	if  args:
		fn = args[0]
		with open(fn) as fd:
			data = fd.read()
	else:
		data = sys.stdin.read()
		fn = ''
	lines, words, chars = get_count(data)
	print_wc(fn, options, lines, words, chars)

main()




