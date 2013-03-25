#! /usr/bin/env python

'''
My python solution to the Pass Triangle problem on code eval
By Cristina Munoz

More info here:
https://www.codeeval.com/open_challenges/89/
'''

# --------
# Imports
# --------

import sys


# ----------
# Functions
# ----------

def parse_and_format_input(file_contents):
    '''
    Converts file content into a matrix like list with zero padding
    '''
    
    data = []
    for line in file_contents:
        line = line.rstrip()
        data.append(map(int, line.split(' ')))

    # base of triangle will be longest, so add zeros to each sub-list to expand them to size of base (last list)
    list_len = len(data[-1]) - 1
    for i in range(list_len):
        data[i].extend([0] * (list_len-i))
    
    return data


def compute_max_path(data):
    '''
    Compute the max sum but starting at the base, and iterating up the triangle, adding the max child to each node
    '''
    rows = len(data[-1]) - 2
    for i in range(rows, -1, -1):
        for j in range(i+1):
            data[i][j] += max(data[i+1][j], data[i+1][j+1])
    
    #return vertex of triangle, which now contains the max sum
    return data[0][0]


# ------
# Main
# ------

def main():
    test_file = open(sys.argv[1], 'r')
    data_list = parse_and_format_input(test_file)
    test_file.close()
    max_sum = compute_max_path(data_list)
    print max_sum


if __name__ == "__main__":
    main()
