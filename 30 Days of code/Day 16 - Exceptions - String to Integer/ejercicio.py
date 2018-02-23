# >>> Day 16: Exceptions - String to Integer
# >>> https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem

#!/bin/python3
import sys

S = '.'#input().strip()

try:
    intValue = int(S)
    print(intValue)
except:
    print('Bad String')
