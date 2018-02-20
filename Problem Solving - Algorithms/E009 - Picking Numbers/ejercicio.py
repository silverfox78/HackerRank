# >>> Picking Numbers
# >>> https://www.hackerrank.com/challenges/picking-numbers/problem

#!/bin/python3

import sys
import itertools

def pickingNumbers(a):
    largo = len(a)
    arreglo = sorted(a)
    x = 0
    for y in range(largo - x, 1, -1):
        diferencia = largo - y + 1
        for z in range(diferencia):
            analisis = arreglo[z:y + z]
            suma = abs(analisis[0] - analisis[y - 1])
            if suma >= 0 and suma <= 1:
                return y

if __name__ == "__main__":
    n = 6 #int(input().strip())
    a = [4,6,5,3,3,1] #list(map(int, input().strip().split(' '))) [1,2,2,3,1,2] #
    result = pickingNumbers(a)
    print(result)
