#Pangrams
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
texto = input().strip()
arreglo = sorted(set(list(texto.upper())))
for i in range(len(arreglo)):
    if arreglo[i] in letras:
        letras.remove(arreglo[i])
print('pangram' if len(letras) == 0 else 'not pangram')