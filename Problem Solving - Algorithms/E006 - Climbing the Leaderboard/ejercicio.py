# >>> Climbing the Leaderboard
# >>> https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

#!/bin/python3
# V1
#     if len(scores) == 0:
#         return [1] * len(alice)

#     retorno = []
#     totalPuntaje = sorted(list(set(map(int, scores))), reverse=True)
#     alicePuntaje = list(map(int, alice))
#     minimo = min(totalPuntaje)
#     maximo = max(totalPuntaje)
#     ultimaPosicion = len(totalPuntaje) + 1

#     for elem in [x for x in alicePuntaje if x <= minimo]:
#         retorno.append(ultimaPosicion)
#         alicePuntaje.remove(elem)
    
#     for elem in [x for x in alicePuntaje if x >= maximo]:
#         retorno.append(1)
#         alicePuntaje.remove(elem)

#     for valor in alicePuntaje:
#         totalPuntaje = [x for x in totalPuntaje if x > valor]
#         retorno.append(len(totalPuntaje) + 1)

#     return sorted(retorno, reverse=True)

import sys

def climbingLeaderboard(scores, alice):
    if len(scores) == 0:
        return [1] * len(alice)

    retorno = []
    totalPuntaje = sorted(list(set(map(int, scores))), reverse=True)
    alicePuntaje = list(map(int, alice))
    minimo = min(totalPuntaje)
    maximo = max(totalPuntaje)
    ultimaPosicion = len(totalPuntaje) + 1

    valoresMenores = len([x for x in alicePuntaje if x < minimo])
    retorno += [1] * valoresMenores

    valoresMayores = len([x for x in alicePuntaje if x >= maximo])
    retorno += [ultimaPosicion] * valoresMayores

    alicePuntaje = alicePuntaje[(valoresMenores):(len(alicePuntaje) - valoresMayores)]

    for valor in alicePuntaje:
        totalPuntaje = [x for x in totalPuntaje if x > valor]
        retorno.append(len(totalPuntaje) + 1)

    return sorted(retorno, reverse=True)

if __name__ == "__main__":
    n = 7 #int(input().strip())
    scores = '100 100 50 40 40 20 10'.split() #list(map(int, input().strip().split(' ')))
    m = 4 #int(input().strip())
    alice = '5 25 50 120'.split() #list(map(int, input().strip().split(' ')))
    result = climbingLeaderboard(scores, alice)
    print ("\n".join(map(str, result)))
