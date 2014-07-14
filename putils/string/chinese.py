#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
This is a tool for opearation on chinese or english with chinese

@Author : Jasonwbw@yahoo.com
'''

import re

def contain_english(s):
	return re.search(ur'[a-zA-Z]+', s) != None

def contain_chinese(s):
	return re.search(ur'[\u4e00-\u9fa5]+', s) != None

if __name__ == '__main__':
	import sys
	reload(sys)
	sys.setdefaultencoding('utf-8')

	# test contain english
	print contain_english(u"abcd sssd;sdfsdfdsfs,")
	print contain_english(u"家人,現在是我生命中的重中之重。下面的文章是98、99年我寫《足音》和 | 《圓人生的夢》時，家人為我写下的文字，我十分珍惜。")
	print contain_english(u"家人aad。")
	print ''

	# test contain chinese
	print contain_chinese(u"abcd sssd;sdfsdfdsfs,")
	print contain_chinese(u"家人,現在是我生命中的重中之重。下面的文章是98、99年我寫《足音》和 | 《圓人生的夢》時，家人為我写下的文字，我十分珍惜。")
	print contain_chinese(u"家人aad。")
	print ''