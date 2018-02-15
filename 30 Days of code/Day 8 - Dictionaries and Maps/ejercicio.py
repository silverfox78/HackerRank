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
            if nombre in diccionario:
                print('{}={}'.format(nombre, str(diccionario[nombre][0])))
            else:
                print('Not found')
        except:
            break

Mejor opcion...
n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break