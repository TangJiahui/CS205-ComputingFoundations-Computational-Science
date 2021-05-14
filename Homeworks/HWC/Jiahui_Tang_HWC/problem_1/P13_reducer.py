#!/usr/bin/python

import sys

previous = None
sum = 0
count = 0

for line in sys.stdin:
    key, value = line.split( '\t' )
    
    if key != previous:
        if previous is not None:
            print previous +  '\t' + str( sum/count )
        previous = key
        sum = 0
        count = 0
    
    sum = sum + float( value )
    count += 1

print previous +  '\t' + str( sum/count )
