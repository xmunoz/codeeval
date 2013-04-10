#! /usr/bin/env python

import sys

def parse_file(f):
    data = []
    for line in f:
        data.append(int(line.rstrip()))

    return data

def is_palindrome(val):
    if val == val[::-1]:
        return True
    return False


def main():
    test_file = open(sys.argv[1], 'r')
    data = parse_file(test_file)
    test_file.close()
    for v in data:
        i = 0
        while not is_palindrome(str(v)):
            v  += int(str(v)[::-1])
            i += 1
        print i, v

if __name__ == "__main__":
    main()
