# >>> Alphabet Rangoli
# >>> https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def printLine(number, large):
    return ('-'*(int((large - (number*4) - 1) / 2))) + ('{}' if number == 0 else '{}-'*number*2 + '{}') + ('-'*(int((large - (number*4) - 1) / 2)))

def print_rangoli(size):
    large = ((size - 1) * 4) + 1
    for x in range(size -1, -1, -1):
        array = [chr(97 + x) for x in range(size - 1, x, -1)]
        array.extend([chr(97 + x) for x in range(x, size, 1)])
        formatLine = printLine(int(len(array) / 2), large)
        print(formatLine.format(*array))
    for x in range(1, size, 1):
        array = [chr(97 + x) for x in range(size - 1, x, -1)]
        array.extend([chr(97 + x) for x in range(x, size, 1)])
        formatLine = printLine(int(len(array) / 2), large)
        print(formatLine.format(*array))


if __name__ == '__main__':
    #n = int(input())
    n = 10
    print_rangoli(n)



