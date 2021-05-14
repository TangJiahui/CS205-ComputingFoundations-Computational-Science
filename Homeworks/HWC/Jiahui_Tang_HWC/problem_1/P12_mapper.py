#!/usr/bin/python
# url regex:https://stackoverflow.com/questions/9760588/how-do-you-extract-a-url-from-a-string-using-python/31952097

import sys

for line in sys.stdin:
    url = line.split(" ")[6]
    print(url + "\t1")

