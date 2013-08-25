#!/usr/bin/python

import sys


def squares(num_squares):
    for num in range(1, num_squares+1):
        print num, num*num

if len(sys.argv) == 1:
    print "usage: squares: <num_squares>"
else:
    squares(int(sys.argv[1]))