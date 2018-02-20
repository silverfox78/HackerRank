# >>> Utopian Tree
# >>> https://www.hackerrank.com/challenges/utopian-tree/problem

#!/bin/python3

import sys

def utopianTree(n):
    altura = 1
    for x in range(n):
        altura += altura if (x % 2 == 0) else 1
        print('x {} - {} - {}'.format(n, x, altura))
    return altura

if __name__ == "__main__":
    t = 5 #int(input().strip())
    arreglo = [0, 1, 2, 3, 4]
    for a0 in range(t):
        n = arreglo[a0] #int(input().strip())
        result = utopianTree(n)
        print(result)