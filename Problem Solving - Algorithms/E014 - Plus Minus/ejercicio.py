# >>> Plus Minus
# >>> https://www.hackerrank.com/challenges/plus-minus/problem

#!/bin/python3

import sys

def plusMinus(arr):
    size = len(arr)
    countPositive = len([x for x in arr if x > 0])
    countNegative  = len([x for x in arr if x < 0])
    countZeroes = len([x for x in arr if x == 0])
    print(format(countPositive/size, '.6f'))
    print(format(countNegative/size, '.6f'))
    print(format(countZeroes/size, '.6f'))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)