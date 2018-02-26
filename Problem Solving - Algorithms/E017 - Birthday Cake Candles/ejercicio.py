# >>> Birthday Cake Candles
# >>> https://www.hackerrank.com/challenges/birthday-cake-candles/problem

#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    array = sorted(ar)
    maxNumber = array[n - 1]
    return array.count(maxNumber)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)