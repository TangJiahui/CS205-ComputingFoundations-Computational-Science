#!/usr/bin/python

import sys
import re

pattern = re.compile(sys.argv[1])

for line in sys.stdin:
    if re.search(pattern, line):
    	print(""+"\t"+line.rstrip('\r\n'))