#!/usr/bin/python

import sys

for line in sys.stdin:
	key, value = line.split('\t')
	print (value.rstrip('\r\n'))