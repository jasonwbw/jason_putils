#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
This is a tool for random select k element from an unknow length data set

@Author : Jasonwbw@yahoo.com
'''

import random

def random_k(iterator, k, need_lefts=False):
	'''
	Random select k element

	Args:
	    iterator   : iterator of data set
	    k          : top k to choose
	    need_lefts : need the result for the lefts datas after random select 

	Returns:
	    list of k element that choosen
	'''
	choosen = []
	unchoosen = [] if need_lefts else None
	for i in xrange(k):
		choosen.append(iterator.next())
	elem = iterator.next()
	idx = k
	while True:
		# random select
		if random.randint(0, idx - 1) < k:
			tmp_idx = random.randint(0, len(choosen) - 1)
			if need_lefts:
				unchoosen.append(choosen[tmp_idx])
			choosen[tmp_idx] = elem
		elif need_lefts:
			unchoosen.append(elem)
		# iterate next element
		try:
			elem = iterator.next()
			idx += 1
		except StopIteration:
			break
	return choosen, unchoosen

if __name__ == '__main__':
	lst = range(10)
	
	it = iter(lst)
	choosen, unchoosen = random_k(it, 3)
	print 'choosen', choosen
	print 'unchoosen', unchoosen
	print ''

	it = iter(lst)
	choosen, unchoosen = random_k(it, 3, need_lefts=True)
	print 'choosen', choosen
	print 'unchoosen', unchoosen