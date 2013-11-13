#!/usr/bin/env python

'''
My python solution to the Mth to last element problem on code eval
By Cristina Munoz

More info here:
    https://www.codeeval.com/open_challenges/10/
'''

import sys

def read_file(filename):
    with open(filename) as f:
        data = f.readlines()
    return data

def main():
    lines = read_file(sys.argv[1])
    for line in lines:
        elements = line.strip('\n').split(' ')
        index_from_last = int(elements[-1]) + 1
        if index_from_last > len(elements):
            pass
        else:
            print elements[-index_from_last]

if __name__ == "__main__":
    main()
