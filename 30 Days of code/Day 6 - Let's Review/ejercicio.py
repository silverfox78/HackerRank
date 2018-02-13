# >>> Day 6: Let's Review
# >>> https://www.hackerrank.com/challenges/30-review-loop/problem

N = int(input())
for i in range(N):
    S = str(input())
    lista = list(S)
    #print (lista[1::2])
    #print (lista[1::])
    #print(lista)
    listaImpar = ''.join(map(str, [y for x,y in enumerate(lista) if x % 2 == 0]))
    listaPar = ''.join(map(str, [y for x,y in enumerate(lista) if x % 2 != 0]))
    print('{} {}'.format(listaImpar, listaPar))

# OFICIAL:
N = int(input())
for i in range(N):
    S = str(input())
    lista = list(S)
    listaImpar = ''.join(map(str, [y for x,y in enumerate(lista) if x % 2 == 0]))
    listaPar = ''.join(map(str, [y for x,y in enumerate(lista) if x % 2 != 0]))
    print('{} {}'.format(listaImpar, listaPar))