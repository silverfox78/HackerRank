#!/bin/python3
import sys

def hackerrankInString(s):
    if s is None:
        return 'NO'
    palabra = 'hackerrank'
    contador = 0
    for i in range(len(s)):
        if s[i] == palabra[contador]:
            contador += 1
            if contador == len(palabra):
                break
    return 'YES' if len(palabra) == contador else 'NO'

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)