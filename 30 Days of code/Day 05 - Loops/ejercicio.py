# >>> Day 5: Loops
# >>> https://www.hackerrank.com/challenges/30-loops/problem
#!/bin/python3

import sys

n = 2 #int(input().strip())
for i in range(1, 11):
    print('{} x {} = {}'.format(n, i, n*i))