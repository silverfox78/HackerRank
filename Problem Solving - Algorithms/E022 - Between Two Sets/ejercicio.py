# >>> Between Two Sets
# >>> https://www.hackerrank.com/challenges/between-two-sets/problem

#!/bin/python3

import sys
import math

def getTotalX(a, b):
    array = []
    final = []
    for x in b:
        maximum = int(math.sqrt(x))
        for y in range(2, x + 1):
            if x % y == 0:
                array.append(y)
    array = sorted(set(array))
    
    for x in a:
        for y in array:
            if y % x == 0:
                final.append(y)
    final = sorted(set(final))
    array = []

    for x in final:
        agregar = True
        for y in b:
            if y % x != 0:
                agregar = False
        if agregar:
            array.append(x)
    array = sorted(set(array))
    print(array)
    print(final)
if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)