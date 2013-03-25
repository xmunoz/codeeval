#! /usr/bin/env python

'''
My python solution to the double squares problem on CodeEval
By Cristina Munoz

More info here:
https://www.codeeval.com/open_challenges/33/
'''

# --------
# Imports
# --------

import sys
from math import sqrt
from math import floor

# ----------
# Functions
# ----------

def parse_file(f):
    data = []
    for line in f:
        data.append(int(line.rstrip()))
    
    #remove first elem, which is just size of d
    data.pop(0)
    return data

def compute_all_squares():
    '''
    Make a list of squares from 0 to max_val
    '''
    max_int = 2147483647
    squares = []
    for i in range(int(sqrt(max_int))):
        squares.append(i**2)

    return squares


def find_num_double_squares(val, squares):
    '''
    Finds the number of ways a value can be expressed as the sum of squares
    '''
    max_square = int(sqrt(val))**2
    max_square_index = squares.index(max_square)
    possible_vals = squares[:max_square_index + 1]
    counter = 0
    for i in possible_vals:
        if (val - i) in possible_vals:
            counter += 1
            if (i == val-i):
              possible_vals.remove(i)
            else:
              possible_vals.remove(i)
              possible_vals.remove(val-i)
    return counter
    
# ------
# Main
# ------

def main():
    test_file = open(sys.argv[1], 'r')
    data = parse_file(test_file)
    print 'data', data
    test_file.close()
    possible_squares = compute_all_squares()
    for d in data:
        print find_num_double_squares(d, possible_squares)


if __name__ == "__main__":
    main()
