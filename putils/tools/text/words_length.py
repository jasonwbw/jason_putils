#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# count how much word in one line, get the statistics result
#
# @Author : Jasonwbw@yahoo.com

import sys

des = '<input file name> [-p parts] [-c threshold]' + \
    '\n\tcompute average word count for each line, default will print out int average length, standard variance, max and min value, total line. ' + \
    '\n\tAnd divide the line into [parts] by word count, parts must large than 1 and odd, default is 2.' + \
    '\n\tAnd you can give threshold to count how much line\'s word count less than it.'

def check_params(argv):
	if len(argv) < 1:
		print 'leak params, please use like:', des
		return False
	return True

def handle(argv, opts):
	# check the params is right or not
	if not check_params(argv):
		return

	# params
	filename = argv[0]
	parts = 2
	threshold = -1
	if opts != None:
		for opt, arg in opts:
			if opt == '-p':
				parts = int(arg)
				if parts % 2 != 0:
					print '[Error] parts should be odd.'
					return
			elif opt == '-c':        
			    threshold = int(arg) 

	# var for count
	total_words, min_words, max_words = 0, sys.float_info.max, 0.0
	min_s, max_s = '', ''
	with open(argv[0], 'r') as fp:
		line_num = 0
		for line in fp:
			sentence = line.strip()
			count = sentence.count(' ') + 1
			if count < min_words:
				min_words, min_s = count, sentence
			if count > max_words:
				max_words, max_s = count, sentence
			total_words += count
			line_num += 1

	# statistics var
	avg, variance = float(total_words) / line_num, 0
	small_one_part, large_one_part = int((avg - min_words) / (parts / 2)) + 1, int((max_words - avg) / (parts / 2)) + 1, 
	part_count = [0] * parts
	threshold_count = 0
	with open(argv[0], 'r') as fp:
		for line in fp:
			count = line.strip().count(' ') + 1
			variance += (count - avg) ** 2
			if count > avg:
				part_count[parts / 2 + int(count - avg) / large_one_part] += 1
			else:
				part_count[int(avg - count) / small_one_part] += 1
			if threshold != -1 and count < threshold:
				threshold_count += 1
	
	# print out result
	print 'The file is total', line_num, 'line.'
	print 'average word count for one line is' , avg
	print 'min word count', min_words
	print 'max word count', max_words
	print 'standard variance is', (variance / float(line_num)) ** 0.5
	print '\ntake the line into', parts, 'parts'
	print_table(min_words, small_one_part, max_words, large_one_part, part_count)
	if threshold != -1:
		print '\nthere are', threshold_count, 'line\'s word count less than', threshold

def print_table(min_words, small_one_part, max_words, large_one_part, part_count):
	for i in xrange(len(part_count) / 2):
		print 'smaller ' + str(min_words + small_one_part * i) + '-' + str(min_words + small_one_part * (i + 1)) + '\t' + str(part_count[i])
	for i in xrange(len(part_count) / 2, 0, -1):
		print 'larger ' + str(max_words - large_one_part * i) + '-' + str(max_words - large_one_part * (i - 1)) + '\t' + str(part_count[len(part_count) - i])


if __name__ == '__main__':
	import getopt
	reload(sys)
	sys.setdefaultencoding('utf-8')
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'c:p:', [])
		handle(args, opts)
	except getopt.GetoptError:
		sys.exit(2)                 