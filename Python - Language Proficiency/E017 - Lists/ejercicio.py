# >>> Lists
# >>> https://www.hackerrank.com/challenges/python-lists/problem

def optionInsert(arguments, array):
    sizeArray = len(array)
    valueArray = list(map(int, arguments))
    if valueArray[0] > sizeArray or valueArray[0] < 0:
        return array
    array.insert(valueArray[0], valueArray[1])
    return array

def optionPrint(arguments, array):
    print(array)
    return array

def optionRemove(arguments, array):
    sizeArray = len(array)
    if sizeArray <= 0:
        return []
    valueArray = list(map(int, arguments))
    array.pop(array.index(valueArray[0]))
    return array

def optionAppend(arguments, array):
    valueArray = list(map(int, arguments))
    array.append(valueArray[0])
    return array

def optionSort(arguments, array):
    return sorted(array)

def optionPop(arguments, array):
    sizeArray = len(array)
    if sizeArray <= 0:
        return []
    array.pop(sizeArray - 1)
    return array

def optionReverse(arguments, array):
    return list(reversed(array))

def processOption(command, arguments, array):
    return {
        'insert': lambda arguments, array: optionInsert(arguments, array),
        'print': lambda arguments, array: optionPrint(arguments, array),
        'remove': lambda arguments, array: optionRemove(arguments, array),
        'append': lambda arguments, array: optionAppend(arguments, array),
        'sort': lambda arguments, array: optionSort(arguments, array),
        'pop': lambda arguments, array: optionPop(arguments, array),
        'reverse': lambda arguments, array: optionReverse(arguments, array)
    }[command](arguments, array)

if __name__ == '__main__':
    N = int(input())
    arreglo = []
    for _ in range(N):
        comando, *argumento = input().split()
        arreglo = processOption(comando, argumento, arreglo)