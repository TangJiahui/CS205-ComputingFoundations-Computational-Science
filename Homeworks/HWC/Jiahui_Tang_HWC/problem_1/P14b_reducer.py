#!/usr/bin/python

import sys

previous = None
id_lst = []

for line in sys.stdin:
    _range, movieId = line.split( '\t' )
    movieId = int(movieId)
    
    if _range != previous:
        if previous is not None:
            print previous   + '\t' + ','.join(id_lst)
        previous = _range
        id_lst = []
    id_lst.append(str(movieId))


print previous   + '\t' + ','.join(id_lst)
