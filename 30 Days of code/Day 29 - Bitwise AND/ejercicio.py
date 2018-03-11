# >>> Day 29: Bitwise AND
# >>> https://www.hackerrank.com/challenges/30-bitwise-and/problem

#!/bin/python3

import sys

def maximumPossible(n, k):
    print(k-1 if ((k-1) | k) <= n else k-2)
    # maximun = 0
    # for x in range(1, n, 1):
    #     for y in range(x + 1, n+1, 1):
    #         tmp = x&y
    #         if tmp < k and tmp > maximun:
    #             maximun = tmp
    # print(maximun)
    
t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    maximumPossible(n, k)