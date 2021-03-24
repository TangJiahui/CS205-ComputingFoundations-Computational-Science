#!/usr/bin/python

import sys

previous = None
summ = 0

for line in sys.stdin:
    key, value = line.split( '\t' )

    if key != previous:
        if previous is not None:
            print(str( summ ) + '\t' + previous)
        previous = key
        summ = 0

    summ = summ + int( value )

print(str( summ ) + '\t' + previous)
