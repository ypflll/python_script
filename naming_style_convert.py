#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Jul 7 2017
@author: pavle
@e-mail: pavle_yao@yahoo.com

This script change code style from exampleName to example_name.
"""

import re


def newpat_func(matched):
    return matched.group()[0] + '_' + matched.group()[1].lower() + matched.group()[2]

def main():

    fr = open('xxx/xxx.c', 'r')
    text = fr.read()

    pattern = re.compile(r"[a-z][A-Z][a-z]")#

    '''
    m = re.match(pattern, text)#match from the first word
    print m

    m = re.search(pattern, text)#search the whole text, return the first match
    print m.group()

    m = re.sub(pattern, 'g_s', text)#relace with a fixed text
    print m

    m = re.findall(pattern, text)
    print m

    for m in re.finditer(pattern, text):#Return an iterator yielding MatchObject instances
    	print m.group()
    '''

    text = re.sub(pattern, newpat_func, text)#The function takes a single match object argument, and returns the replacement string.

    fr.close()

    fr = open('xxx/xxx.c', 'w')
    fr.write(text)
    fr.close()

if __name__ == '__main__':
    main()

