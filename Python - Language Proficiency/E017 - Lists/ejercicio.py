# >>> Lists
# >>> https://www.hackerrank.com/challenges/python-lists/problem

def opcion(comando, argumentos, arreglo):
    arr = arreglo
    arg = list(argumentos)
    largo = len(arr)
    if comando == 'insert':
        arr.insert(int(arg[0]), int(arg[1]))
    if comando == 'print':
        print(arr)
    if comando == 'remove':
        if largo == 0:
            return arr
        arr.pop(arr.index(int(arg[0])))
    if comando == 'append':
        arr.append(int(arg[0]))
    if comando == 'sort':
        return sorted(arr)
    if comando == 'pop':
        if largo == 0:
            return arr
        arr.pop(len(arr) - 1)
    if comando == 'reverse':
        return sorted(arr, reverse=True)
    return arr

if __name__ == '__main__':
    N = int(input())
    arreglo = []
    for _ in range(N):
        comando, *argumento = input().split()
        arreglo = opcion(comando, argumento, arreglo)