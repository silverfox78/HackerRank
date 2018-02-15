# >>> Climbing the Leaderboard
# >>> https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

#!/bin/python3

import sys

def climbingLeaderboard(scores, alice):
    if len(scores) == 0:
        return [1] * len(alice)

    if len(alice) == 0:
        return []

    retorno = []
    totalPuntaje = sorted([int(x) for x in set(scores)])
    ultimaPosicion = len(totalPuntaje) + 1
    minimo = totalPuntaje[0]
    maximo = totalPuntaje[ultimaPosicion-2]

    contador = 0
    for i in alice:
        if int(i) < minimo:
            contador += 1
        else:
            break
    alice = alice[contador:]
    retorno += [ultimaPosicion] * contador

    for i in alice:
        if int(i) > maximo:
            retorno.append(1)

    alice = alice[:ultimaPosicion - contador - 2]

    for valor in [int(x) for x in alice]:
        contador = 0
        for elem in totalPuntaje:
            if valor < elem:
                ultimaPosicion -= contador
                totalPuntaje = totalPuntaje[contador:]
                retorno.append(ultimaPosicion)
                break
            contador += 1
    return sorted(list(retorno), reverse=True)

if __name__ == "__main__":
    n = 7 #int(input().strip())
    scores = '100 100 50 40 40 20 10'.split() #list(map(int, input().strip().split(' ')))
    m = 4 #int(input().strip())
    alice = '5 25 50 120'.split() #list(map(int, input().strip().split(' ')))
    #result = climbingLeaderboard(scores, alice)

    scores = map(int, scores)
    alice = map(int, alice)
    leaderboard = sorted(set(scores), reverse = True)
    l = len(leaderboard)

    for a in alice:
        while (l > 0) and (a >= leaderboard[l-1]):
            l -= 1
        print(l+1)

    #print ("\n".join(map(str, result)))