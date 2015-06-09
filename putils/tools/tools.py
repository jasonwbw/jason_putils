#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
This is a tool interface for all tools

@Author : Jasonwbw@yahoo.com
'''

import sys

import compile
import words_length

des = [
    ('nlp wl', 'nlp wl ' + compile.des, 'func_words_length'),
]

def description():

def func_words_length(argv):
	pass

if __name__ == '__main__':
	import tools as t
	funcs = b.__dict__.items()
    for func_name, func in  b.__dict__.items():
        if func_name.startswith('func_'):
            counter = func(sys.argv[1:])