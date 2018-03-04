if __name__ == "__main__":
    n = int(input().strip())
    diccionario = {}
    consultas = []
    for _ in range(n):
        nombre, *numero = input().split()
        diccionario[nombre] = numero
    for _ in range(n):
        consultas.append(str(input().strip()))
    for query in consultas:
        resultado = diccionario.get(query, None)
        if resultado is None:
            print('Not found')
        else:
            print('{}={}'.format(query, int(resultado[0])))