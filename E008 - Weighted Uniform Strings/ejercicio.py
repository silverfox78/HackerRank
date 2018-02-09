#Weighted Uniform Strings
#!/bin/python3
import sys


s = input().strip() #s = 'abccddde'
n = int(input().strip()) #n = [6, 1, 3, 12, 5, 9, 10]
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cadenas = [letras.index(s[0]) + 1]
previo = s[0]
for i in range(1, len(s)):
    if previo[0] == s[i]:
        previo += s[i]
        cadenas.append((letras.index(previo[0]) + 1) * len(previo))
    else:
        previo = s[i]
        cadenas.append((letras.index(previo[0]) + 1) * len(previo))
cadenas = set(cadenas)
for a0 in range(n): #for a0 in range(len(n)):
    x = int(input().strip()) #x = n[a0]
    print('Yes' if x in cadenas else 'No')