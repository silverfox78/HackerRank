# >>> Electronics Shop
# >>> https://www.hackerrank.com/challenges/electronics-shop/problem

#!/bin/python3
import sys

def getMoneySpent(keyboards, drives, s):
    costs = [(x + y) for x in keyboards for y in drives]
    costs = sorted([x for x in costs if x <= s], reverse=True)
    return costs[0] if len(costs) > 1 else -1

#Caso I
s = 10
n = 2
m = 3
keyboards = [3, 1]
drives = [5, 2, 8]
# s,n,m = input().strip().split(' ')
# s,n,m = [int(s),int(n),int(m)]
# keyboards = list(map(int, input().strip().split(' ')))
# drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
