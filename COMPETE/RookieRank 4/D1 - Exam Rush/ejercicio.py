# >>> Exam Rush
# >>> https://www.hackerrank.com/contests/rookierank-4/challenges/exam-rush

#!/bin/python3

import sys

def examRush(tm, t):
    contador = 0
    horas = t
    for libro in sorted(tm):
        #print('Libro: {} - Horas: {} - Contador: {}'.format(libro, horas, contador))
        horas -= libro
        if horas < 0:
            break
        else:
            contador += 1
    return contador

if __name__ == "__main__":
    #n, t = input().strip().split(' ')
    n, t = [2, 5] #[int(n), int(t)]
    tm = [5, 2, 1, 2]
    tm_i = 0
    # for tm_i in range(n):
    #    tm_t = int(input().strip())
    #    tm.append(tm_t)
    result = examRush(tm, t)
    print(result)
