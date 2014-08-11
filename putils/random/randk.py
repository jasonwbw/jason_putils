#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
This is a tool for random select k element from an unknow length data set

@Author : Jasonwbw@yahoo.com
'''

import random

def random_k(iterator, k):
	'''
	Random select k element

	Args:
	    iterator : iterator of data set
	    k        : top k to choose

	Returns:
	    list of k element that choosen
	'''
	choosen = []
	for i in xrange(k):
		choosen.append(iterator.next())
	elem = iterator.next()
	idx = k
	while True:
		if random.randint(0, idx - 1) < k:
			choosen[random.randint(0, len(choosen) - 1)] = elem
		try:
			elem = iterator.next()
			idx += 1
		except StopIteration:
			break
	return choosen

if __name__ == '__main__':
	lst = range(10)
	it = iter(lst)
	print random_k(it, 2)