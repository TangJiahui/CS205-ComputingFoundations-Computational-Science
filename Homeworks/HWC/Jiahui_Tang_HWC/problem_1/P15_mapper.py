#!/usr/bin/python

import sys
from csv import reader

for line_lst in reader(sys.stdin):
	m_type = line_lst[3]
	mass = line_lst[4]
	# ignore record if there's null value in mass or type
	if m_type != "" and mass != "":
		print(m_type + "\t" + mass)