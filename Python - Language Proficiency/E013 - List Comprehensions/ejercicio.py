# >>> List Comprehensions
# >>> https://www.hackerrank.com/challenges/list-comprehensions/problem
import itertools

if __name__ == '__main__':
    x = 1 #int(input())
    y = 1 #int(input())
    z = 1 #int(input())
    n = 2 #int(input())

    listaX = list(range(x + 1))
    listaY = list(range(y + 1))
    listaZ = list(range(z + 1))

    arreglo = [listaX, listaY, listaZ]
    combinacion = list(itertools.product(*arreglo))
    resultado = [list(elem) for elem in combinacion if elem[0] + elem[1] + elem[2] != n]
    print(resultado)