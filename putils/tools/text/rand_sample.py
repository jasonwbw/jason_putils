#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
This is a tool for random select x1%, x2%, .. data from file 

@Author : Jasonwbw@yahoo.com
'''

import sys
import random
from utils import count_line

def random_sample(filename, output_filename, xs):
	'''
	Random select x% data from file 

	Args:
	    filename        : file name of data set
	    output_filename : file name to save data
	    xs              : rates
	'''
	lines = count_line(filename)
	rates = []
	assert sum(xs) == 100
	fos = []
	for i, x in enumerate(xs):
		rates.append(sum(xs[:i+1]))
		fos.append(open(output_filename + "_" + str(x) + '.txt', 'w'))
	with open(filename, 'r') as fp:
		line_num = 0
		for line in fp:
			line_num += 1
			rand_res = random.randint(0, 99)
			for i, rate in enumerate(rates):
				if rand_res < rate:
					fos[i].write(line)
					break
	for fo in fos:
		fo.close()


if __name__ == '__main__':
	filename, output_filename = sys.argv[1], sys.argv[2]
	xs = []
	for i in xrange(3, len(sys.argv)):
		xs.append(int(sys.argv[i]))
	random_sample(filename, output_filename, xs)