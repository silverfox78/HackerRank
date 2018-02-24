# >>> Diagonal Difference
# >>> https://www.hackerrank.com/challenges/diagonal-difference/problem

#!/bin/python3

import sys

def diagonalDifference(a):
    size = len(a)
    sumEjeLeft = sum(a[x][size - x - 1] for x in range(size))
    sumEjeRigth = sum(a[size - x - 1][size - x - 1] for x in range(size))
    return abs(sumEjeLeft - sumEjeRigth)
    

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)