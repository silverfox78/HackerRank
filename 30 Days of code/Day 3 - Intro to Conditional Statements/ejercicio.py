# >>> Day 3: Intro to Conditional Statements
# >>> https://www.hackerrank.com/challenges/30-conditional-statements/problem

#!/bin/python3
import sys

#N = int(input().strip())
N = 24
if N % 2 != 0:
    print('Weird')
else:
    if N >= 6 and N <= 20:
        print('Weird')
    else:
        print('Not Weird')
