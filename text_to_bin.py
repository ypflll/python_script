#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Jul 7 2017
@author: pavle
@e-mail: pavle_yao@yahoo.com

This script reads a text file and save to bin file.
"""

import struct

def endian_swap(s):
    if len(s) != 8:
        print 'Byte length must be 4.'
    else:
        return s[6]+s[7]+s[4]+s[5]+s[2]+s[3]+s[0]+s[1]

def main():
    src_file = 'xxx/xxx.txt'
    dst_file = 'xxx/xxx.bin'

    f_in = open(src_file)
    sss = f_in.read()
    f_out = open(dst_file)

    #remove enter and tab
    ss = []
    for s in sss:
        if s != '\t' and s != '\n':
            ss.append(s)

    #length must be multiple of 8
    if 0 != len(ss)%8:
        for i in range(8 - len(ss)%8):
            ss += '00'

    for i in range(len(ss)/8):
        s = ss[i*8:i*8+8]
        s = endian_swap(s)
        s = int(s, base = 16)
        byte = struct.pack('I', s)
        f_out.write(byte)

    f_out.close()

if __name__ == '__main__':
    main()
