#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# remove stopwords by give stopwords list
#
# @Author : Jasonwbw@yahoo.com

import sys
import utils

des = r'<input file name> <output file name> <stopwords file name>' + \
    r'\n\tfilter input file to remove all stopwords(that stopwords in file extended with \\stchost-153\bowwu\data\stopwords.txt)' + \
    r'\n\twe will keep the tab format.' + \
    r'\n\tstopwords file name can be null.'

def check_params(argv):
	if len(argv) < 2:
		print 'leak params, please use like:', des
		return False
	return True

def handle_with_argv(argv, opts):
	# check the params is right or not
	if not check_params(argv):
		return

	# params
	input_f, output_f = argv[0], argv[1]
	handle(input_f, output_f, argv[2] if len(argv) == 3 else None)

def handle(input_f, output_f, stopwords_f=None):
	# load stopwords
	stopwords = set(utils.load_word_list(r'\\stchost-153\bowwu\data\stopwords.txt'))
	if stopwords_f != None:
		stopwords = stopwords.union(set(utils.load_word_list(stopwords_f)))

	# count input
	count = utils.count_line(input_f)
	print 'input file contains %d lines' % count 

	# filter
	with open(input_f, 'r') as fin:
		with open(output_f, 'w') as fout:
			line_count = 0
			for line in fin:
				# log
				line_count += 1
				if line_count % (count / 10) == 0:
					print 'handled %d%%' % (line_count * 100 / count + 1)
					fout.flush()
				# func
				elements = line.strip().split('\t')
				for i, element in enumerate(elements):
					fout.write(' '.join([w for w in element.split(' ') if not w in stopwords]) + ('\t' if i < len(elements) - 1 else '\n'))

if __name__ == '__main__':
	import getopt
	reload(sys)
	sys.setdefaultencoding('utf-8')
	try:
		opts, args = getopt.getopt(sys.argv[1:], '', [])
		handle_with_argv(args, opts)
	except getopt.GetoptError:
		sys.exit(2)                 