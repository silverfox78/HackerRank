# >>> Mini-Max Sum
# >>> https://www.hackerrank.com/challenges/mini-max-sum/problem

#!/bin/python3

import sys
import itertools

def miniMaxSum(arr):
    minNumber = None
    maxNumber = None    
    options = [sum(x) for x in itertools.combinations(arr, 4)]
    sizeOptions = len(options)
    results = sorted(options)
    minNumber = results[0]
    maxNumber = results[sizeOptions - 1]
    print('{} {}'.format(minNumber, maxNumber))

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
