# >>> Day 20: Sorting
# >>> https://www.hackerrank.com/challenges/30-sorting/problem

#!/bin/python3

import sys

n = 3 #int(input().strip())
a = [3, 2, 1] #list(map(int, input().strip().split(' ')))

countSwaps = 0
firstElement = None
lastElement = None
tmp = None

for x in range(0, n , 1):
    for y in range(x + 1, n, 1):
        #print('»» [{} , {}]'.format(x, y))
        if a[x] > a[y]:
            #print('{}.- >>> {} - {} - [{}, {}]'.format(countSwaps, a[x], a[y], x, y))
            tmp = a[x]
            a[x] = a[y]
            a[y] = tmp
            countSwaps += 1
            
firstElement = a[0]
lastElement = a[n - 1]

print('Array is sorted in {} swaps.'.format(countSwaps))
print('First Element: {}'.format(firstElement))
print('Last Element: {}'.format(lastElement))