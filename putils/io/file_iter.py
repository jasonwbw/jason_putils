#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
This is a tool for file iterate

@Author : Jasonwbw@yahoo.com
'''

import numpy
from itertools import izip

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def to_unicode(text, encoding='utf8', errors='strict'):
    """Convert a string (bytestring in `encoding` or unicode), to unicode."""
    if isinstance(text, unicode):
        return text
    return unicode(text, encoding, errors=errors)

class LineSentence(object):
    """Simple format: one sentence = one line; words already preprocessed and separated by whitespace."""

    def __init__(self, source):
        """
        `source` can be either a string or a file object.
        Example:
            sentences = LineSentence('myfile.txt')
        """
        self.source = source

    def __iter__(self):
        """Iterate through the lines in the source."""
        with open(self.source, 'rb') as fin:
            for line in fin:
                yield to_unicode(line)