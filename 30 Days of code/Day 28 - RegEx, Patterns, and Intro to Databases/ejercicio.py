# >>> Day 28: RegEx, Patterns, and Intro to Databases
# >>> https://www.hackerrank.com/challenges/30-regex-patterns/problem

#!/bin/python3

import sys
import re

arrayName = []
N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    searchObj = re.search( r'@gmail.com', emailID, re.M|re.I)
    if searchObj:
        arrayName.append(firstName)
print("\n".join(sorted(arrayName)))