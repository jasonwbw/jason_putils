#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# compile python file to pyc file
#
# @Author : Jasonwbw@yahoo.com

import sys

des = '<input file name>' + \
    '\n\taverage word counting'

def check_params(argv):
	if len(argv) < 1:
		print 'leak params, please use like:', des
		return False
	return True

def handle(argv, opts):
	# check the params is right or not
	if not check_params(argv):
		return

    import py_compile
	py_compile.compile(argv[0])

if __name__ == '__main__':
	import getopt
	reload(sys)
	sys.setdefaultencoding('utf-8')
	try:
		handle(sys.argv[1:], None)
	except getopt.GetoptError:
		sys.exit(2)  