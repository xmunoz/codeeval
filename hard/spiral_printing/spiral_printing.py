#! /usr/bin/env python

'''
My python solution to the spiral printing problem on CodeEval
By Cristina Munoz

More info here:
https://www.codeeval.com/open_challenges/57/
'''


import sys
import re

'''
Parse file, store as matrix-style list
'''
def parse_line(line):
    elems = re.split(';', line.rstrip())
    dim =  [int(x) for x in elems[:2]]
    vals = re.split(' ', str(elems.pop(2)))
    matrix = []
    if dim[0] * dim[1] == len(vals):
        for i in range(dim[0]):
            matrix.append(vals[(i*dim[1]):dim[1]*(1+i)])
        return matrix
    else:
        return False
    
'''
Compute spiral output clockwise with 4 cases: top, right, bottom, left 
'''
def spiral_output(matrix):
    str_vals = ''
    while matrix:
        matrix, str_vals = pop_row(matrix, str_vals, 0)
        if not matrix:
            return str_vals
        matrix, str_vals = pop_col(matrix, str_vals, -1)
        if not matrix:
            return str_vals
        matrix, str_vals = pop_row(matrix, str_vals, -1)
        if not matrix:
            return str_vals
        matrix, str_vals = pop_col(matrix, str_vals, 0)
    
    return str_vals

'''
Removes first or last row, depending on n
'''
def pop_row(matrix, strv, n):
    new_str = []
    for x in matrix[n]:
        new_str.append(x)
    
    if n == -1:
        new_str.reverse()
    
    strv = strv + ' ' + ' '.join(new_str)
    
    return matrix[n+1:len(matrix)+n], strv

'''
Removes first or last column, depending on n
'''
def pop_col(matrix, strv, n):
    new = []
    new_str = []
    for a in matrix:
        new_str.append(a[n])
        new.append(a[n+1:len(matrix[0]) + n])
    
    if n == 0:
        new_str.reverse()
    
    strv = strv + ' ' + ' '.join(new_str)
    return new, strv

def main():
    test_file = open(sys.argv[1], 'r')
    for line in test_file:
        matrix = parse_line(line)
        if matrix:
            print spiral_output(matrix).strip()
        else:
            print 'Bad data'
    test_file.close()

if __name__ == "__main__":
    main()
