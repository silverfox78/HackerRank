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
    totalPuntaje = sorted(list(set(map(int, scores))), reverse=True)
    alicePuntaje = list(map(int, alice))
    ultimaPosicion = len(totalPuntaje) + 1
<<<<<<< HEAD

    valoresMenores = len([x for x in alicePuntaje if x < minimo])
    retorno += [1] * valoresMenores

    valoresMayores = len([x for x in alicePuntaje if x >= maximo])
    retorno += [ultimaPosicion] * valoresMayores

=======
    minimo = totalPuntaje[ultimaPosicion-2]
    maximo = totalPuntaje[0]
    
    valoresMenores = len([x for x in alicePuntaje if x < minimo])
    retorno += [ultimaPosicion] * valoresMenores
    valoresMayores = len([x for x in alicePuntaje if x >= maximo])
    retorno += [1] * valoresMayores
>>>>>>> b089589f17218b0bd752bd822f74478a2660c32c
    alicePuntaje = alicePuntaje[(valoresMenores):(len(alicePuntaje) - valoresMayores)]
    listaPuntajes = sorted(totalPuntaje)
    for valor in alicePuntaje:
<<<<<<< HEAD
        totalPuntaje = [x for x in totalPuntaje if x > valor]
        retorno.append(len(totalPuntaje) + 1)

    return sorted(retorno, reverse=True)
=======
        contador = 0
        for elem in listaPuntajes:
            if valor < elem:
                ultimaPosicion -= contador
                listaPuntajes = listaPuntajes[contador:]
                retorno.append(ultimaPosicion)
                break
            contador += 1
    return sorted(list(retorno), reverse=True)
>>>>>>> b089589f17218b0bd752bd822f74478a2660c32c

if __name__ == "__main__":
    n = 7 #int(input().strip())
    scores = '100 100 50 40 40 20 10'.split() #list(map(int, input().strip().split(' ')))
    m = 4 #int(input().strip())
    alice = '5 25 50 120'.split() #list(map(int, input().strip().split(' ')))
    result = climbingLeaderboard(scores, alice)
    print ("\n".join(map(str, result)))
