# >>> Day 8: Dictionaries and Maps
# >>> https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

#!/bin/python3
if __name__ == "__main__":
    n = int(input().strip())
    diccionario = {}
    for _ in range(n):
        nombre, *numero = input().split()
        diccionario[nombre] = numero
    for _ in range(n):
        try:
            nombre = str(input().strip())
            #resultado = diccionario.get(query, None)
            if nombre in diccionario:
                print('{}={}'.format(nombre, str(diccionario[nombre][0])))
            else:
                print('Not found')
        except:
            break