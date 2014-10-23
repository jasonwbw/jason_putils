#! /usr/bin/env python
#-*- coding: utf-8 -*-

'''
This is a tool for solve the Longest common subsequence problem with the dynamic programming

@Author : Jasonwbw@yahoo.com
'''

def lcs_len(s1, s2):
    '''
    LCS by 2d matrix dp

    Args:
        s1 : list or string
        s2 : list or string

    Returns:
        Longest common subsequence
    '''
    if s1 == None or s2 == None: return 0
    len1, len2 = len(s1), len(s2)
    dp = [ [0 for i in xrange(len2 + 1)] for j in xrange(len1 + 1)]
    for i in xrange(len1):
        for j in xrange(len2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[len1][len2]

def lcs_len_effective(s1, s2):
    '''
    LCS by two 1d matrix dp

    Args:
        s1 : list or string
        s2 : list or string

    Returns:
        Longest common subsequence
    '''
    if s1 == None or s2 == None: return 0
    len1, len2 = len(s1), len(s2)
    dp_i, dp_j = [0 for i in xrange(len2 + 1)], [0 for i in xrange(len1 + 1)]
    for i in xrange(len1):
        dp_it, dp_jt = dp_i, dp_j
        for j in xrange(len2):
            if s1[i] == s2[j]:
                dp_i[j + 1] = dp_j[i + 1] = dp_it[j] + 1
            else:
                dp_i[j + 1] = dp_j[i + 1] = max(dp_it[j + 1], dp_jt[i + 1]) 
    return dp_i[-1]

def lcs_len_res(s1, s2):
    '''
    LCS by 2d matrix dp, and get one result

    Args:
        s1 : list or string
        s2 : list or string

    Returns:
        one of the Longest common subsequence
    '''
    if s1 == None or s2 == None: return 0
    len1, len2 = len(s1), len(s2)
    dp = [ [0 for i in xrange(len2 + 1)] for j in xrange(len1 + 1)]
    for i in xrange(len1):
        for j in xrange(len2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    i, j = len1 - 1, len2 - 1
    res = ''
    while i >= 0 and j >= 0:
        if s1[i] == s2[j]:
            res = s1[i] + res
            i -= 1
            j -= 1
        elif dp[i][j + 1] > dp[i + 1][j]:
            i -= 1
        else:
            j -= 1
    return res

if __name__ == '__main__':
    print lcs_len('adcde', 'acde')
    print lcs_len('a', 'a')
    print lcs_len_effective('adcde', 'acde')
    print lcs_len_effective('a', 'a')
    print lcs_len_res('adcde', 'acde')
    print lcs_len_res('a', 'a')