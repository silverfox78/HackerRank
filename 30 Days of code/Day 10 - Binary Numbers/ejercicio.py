# >>> Day 10: Binary Numbers
# >>> https://www.hackerrank.com/challenges/30-binary-numbers/problem

#!/bin/python3

import sys

def maximo(binario, posicion, valor, tmp):
    v_tmp = tmp
    v_valor = valor
    if binario[posicion] == '1':
        v_tmp += 1
    else:
        v_valor = valor if valor > tmp else tmp
        v_tmp = 0

    if posicion == len(binario) - 1:
        return v_valor if v_valor > v_tmp else v_tmp
    else:
        return maximo(binario, posicion + 1, v_valor, v_tmp)

def secuenciaBinaria(n):
    return maximo('{0:b}'.format(n), 0, 0, 0)

n = 7#int(input().strip())
print(secuenciaBinaria(n))
