#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
This is a tool for tokenize english sentences

@Author : Jasonwbw@yahoo.com
'''

from nltk.tokenize import RegexpTokenizer

class RegexTokenizer(object):

	'''
	Tokenize sentence by separators, default is \w+|\$[\d\.]+|\S+
	'''

	def __init__(self, append_regexs = []):
		'''
		Init

		Args:
		    append_regexs : add more regex elements
		'''
		regex = ur'\w+|\$[\d\.]+|\S+'
		if len(append_regexs) > 0: regex += ur'|'+ ur'|'.join(append_regexs)
		self._tokenizer = RegexpTokenizer(regex)

	def tokenize(self, s):
		'''
		Tokenize the give string

		Args:
		    s : the given string

		Returns:
		    tokenized string
		'''
		return ' '.join(self.tokenize2list(s))

	def tokenize2list(self, s):
		'''
		Tokenize the give string

		Args:
		    s : the given string

		Returns:
		    list after tokenized
		'''
		return self._tokenizer.tokenize(s.decode('utf8'))

if __name__ == '__main__':
	# test multi separator
	s = "aa, bb. dd! cc? ee<< dd> #ss it's 'xx yy\" mm (aa)"
	print RegexTokenizer().tokenize(s)