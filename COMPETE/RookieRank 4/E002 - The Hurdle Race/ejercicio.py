# >>> The Hurdle Race
# >>> https://www.hackerrank.com/challenges/the-hurdle-race/problem
# #!/bin/python3

import sys

def hurdleRace(k, height):
    maximo = k
    posiones = 0
    for elem in height:
        if elem > maximo:
            posiones += elem - maximo
            maximo = elem
    return posiones

if __name__ == "__main__":
    #n, k = input().strip().split(' ')
    n, k = [5, 4] #[int(n), int(k)]
    height = [1, 6, 3, 5, 2] #list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)