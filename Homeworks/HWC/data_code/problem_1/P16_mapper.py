#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    if "5.0" in line:
    	print(""+"\t"+line.rstrip('\r\n'))