#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# count uniques seperated by '\t'
#
# @Author : Jasonwbw@yahoo.com

import sys

des = '<input file name>' + \
    '\n\tcount uniques seperated by \'\t\'.'

def check_params(argv):
	if len(argv) < 1:
		print 'leak params, please use like:', des
		return False
	return True

def handle(argv, opts):
	# check the params is right or not
	if not check_params(argv):
		return

	sets = set()
	with open(argv[0], 'r') as fp:
		line_num = 0
		for line in fp:
			sentence = line.strip()
			for s in line.strip().split('\t'):
				sets.add(s)
			line_num += 1
	
	# print out result
	print 'The file is total', line_num, 'line.'
	print 'unique elements are' , len(sets)

if __name__ == '__main__':
	import getopt
	reload(sys)
	sys.setdefaultencoding('utf-8')
	try:
		opts, args = getopt.getopt(sys.argv[1:], '', [])
		handle(args, opts)
	except getopt.GetoptError:
		sys.exit(2)                 