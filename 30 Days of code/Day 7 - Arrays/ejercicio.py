# >>> Day 7: Arrays
# >>> https://www.hackerrank.com/challenges/30-arrays/problem

#!/bin/python3

import sys


#n = int(input().strip())
arr = '1 4 3 2'.split(' ') #[int(arr_temp) for arr_temp in input().strip().split(' ')]
print(' '.join([str(x) for x in reversed(arr)]))
