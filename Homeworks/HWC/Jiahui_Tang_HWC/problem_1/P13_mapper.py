#!/usr/bin/python

import sys

for line in sys.stdin:
    column = line.split(",")
    year = column[0][:4]
    close_price = column[4]

    print(year + "\t" + close_price)