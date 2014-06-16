#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
This is a tool for opearation on string

@Author : Jasonwbw@yahoo.com
'''

def multi_separator_split(s, separators = set([])):
	'''
	Split str with multi separator

	Args:
	    s : the norm string
	    separators : a set or list of seprator
	
	Returns:
	    a list of string which split by all the separators
	'''
	res = []
	pre_index = 0
	for i in xrange(len(s)):
		if s[i] in separators:
			if i != pre_index:
				res.append(s[pre_index : i])
			pre_index = i + 1
	if pre_index != len(s):
		res.append(s[pre_index : ])
	return res

if __name__ == '__main__':
	# test multi separator
	print multi_separator_split("abcd sssd;sdfsdfdsfs,", separators = set([' ', ';', ',']))
	print multi_separator_split(";abcd ", separators = set([' ', ';', ',']))
	print multi_separator_split("; ,", separators = set([' ', ';', ',']))
	print multi_separator_split(u"家人,現在是我生命中的重中之重。下面的文章是98、99年我寫《足音》和 | 《圓人生的夢》時，家人為我写下的文字，我十分珍惜。".decode('utf-8'), \
		separators = set([u'。'.decode('utf-8'), u'！'.decode('utf-8'), u'？'.decode('utf-8')]))