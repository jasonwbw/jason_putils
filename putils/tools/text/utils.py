#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# utils for file action
#
# @Author : Jasonwbw@yahoo.com

def count_line(filename):
	count = -1
	for count, line in enumerate(open(filename, 'rU')):
		pass
	count += 1
	return count
# end count line

def load_word_list(filename):
	words = []
	with open(filename, 'r') as fp:
		for line in fp:
			words.append(line.strip())
	return words
# end load word list