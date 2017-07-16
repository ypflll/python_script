#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Jul 11 2017
@author: pavle
@e-mail: pavle_yao@yahoo.com

This script read several bin files, add head to each and save to a specified address.
"""
import os
import glob as glob

address = {
    'name1':0x00000000
}

ADDRESS_SIZE = 0XFFFFFFFF

def add_head(data):
    length = len(data)
    head1 = chr(length >> 24) + chr(length >> 16 & 0xff) + chr(length >> 8 & 0xff) + chr(length & 0xff)
    
    check = 0
    for i in range(length/4):
        check += data[i*4] << 24 | data[i*4+1] << 16 | data[i*4+2] << 8 | data[i*4+3]
    check &= 0xffffffff
    head2 = chr(check >> 24) + chr(check >> 16 & 0xff) + chr(check >> 8 & 0xff) + chr(check & 0xff)

    data = head1 + head2 + data
    return data

def main():
    src_path = 'xxx/xxx'
    bin_files = glob.glob(src_path + '*')
    bin_files.sort()

    out_put = bytearray([0 for i in range(ADDRESS_SIZE)])
    for bin_file in bin_files:
        f_in = open(bin_file,'rb')
        s = f_in.read()
        data = bytearray(s)
        if 0 != len(s)%4:
            for i in range(4 - len(s)%4):
                data.append(0)

        data = add_head(head)

        key = bin_file.split('/')[-1]
        out_put[address[key]:address[key]+len(data)-1] = data[:]

    f_out = open('xxx.bin','wb')
    f_out.write(out_put)
    f_out.close()

if __name__ == '__main__':
    main()