# >>> Day 11: 2D Arrays
# >>> https://www.hackerrank.com/challenges/30-2d-arrays/problem

#!/bin/python3

import sys

def analizaMatriz(arr, x, y, maximo):
    suma = arr[x][y] + arr[x][y + 1] + arr[x][y + 2] + arr[x+1][y + 1] + arr[x+2][y] + arr[x+2][y + 1] + arr[x+2][y + 2]
    #print('{}\t{}\t{}\n\t{}\n{}\t{}\t{}'.format(arr[x][y], arr[x][y + 1],arr[x][y + 2],arr[x+1][y + 1],arr[x+2][y],arr[x+2][y + 1],arr[x+2][y + 2]))
    valor = maximo if maximo > suma else suma
    if x ==0 and y == 0:
        valor = suma
    #print('La suma es: {} - el maximo es: {} - el valor es: {}'.format(suma, maximo, valor))
    termino = x == 3 and y == 3
    if termino:
        return valor
    else:
        indiceX = x
        indiceY = y
        if indiceY == 3:
            indiceX += 1
            indiceY = 0
        else:
            indiceY += 1
        return analizaMatriz(arr, indiceX, indiceY, valor)

arr = []
# for arr_i in range(6):
#    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#    arr.append(arr_t)
#arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
arr = [[-1, -1, 0 ,-9 ,-2 ,-2],[-2, -1, -6, -8, -2, -5],[-1, -1, -1, -2, -3, -4],[-1, -9, -2, -4, -4, -5],[-7, -3, -3, -2, -9, -9],[-1, -3, -1, -2, -4, -5]]
print(arr)
total = analizaMatriz(arr, 0, 0, 0)
print(total)