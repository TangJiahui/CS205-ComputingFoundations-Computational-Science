#!/usr/bin/python

import sys

for line in sys.stdin:
    column = line.split(",")
    movieId,rating = column[1],column[2]
    
    print(movieId + "\t" + rating)
