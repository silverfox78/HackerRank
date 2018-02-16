# >>> Organizing Containers of Balls
# >>> https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

#!/bin/python3
import sys

def organizingContainers(container):
    largo = len(container)
    for bola in range(largo):
        print(' - '.join([('B' + str(y) + '[' + str(x) + ']') for x, y in container[bola]]))
        print('Contenedor {}'.format(bola + 1))
    print(container)

if __name__ == "__main__":
    contenedores = [2, 2]
    informacion = [
        [[1, 1], [1, 1]],
        [[0, 2], [1, 1]]
    ]
    q = 2 #int(input().strip())
    for a0 in range(q):
        n = contenedores[a0] #int(input().strip())
        container = []
        for container_i in range(n):
           #container_t = [int(container_temp) for container_temp in input().strip().split(' ')]
           #container.append(container_t)
           container.append(informacion[a0][container_i])
        result = organizingContainers(container)
        print(result)