#!/usr/bin/python

import sys

for line in sys.stdin:
    movieId, rating = line.split("\t")
    rating = float(rating)
    if rating <= 1:
    	print ("Range 1" + "\t" + movieId)
    elif rating <= 2:
    	print ("Range 2" + "\t" + movieId)
    elif rating <= 3:
    	print ("Range 3" + "\t" + movieId)
    elif rating <= 4:
    	print ("Range 4" + "\t" + movieId)
    elif rating <= 5:
    	print ("Range 5" + "\t" + movieId)
