# >>> Staircase
# >>> https://www.hackerrank.com/challenges/staircase/problem

#!/bin/python3

import sys

def staircase(n):
    for x in range(n):
        sizeChar = x + 1
        print('{}{}'.format(' ' * (n - sizeChar), '#' * sizeChar))

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)