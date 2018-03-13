# >>> Alphabet Rangoli
# >>> https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def printLine(number, large):
    lineNumber = int(((large - 1) / 4) + 1) - number
    letterNumber = 97 + number
    print('{} {} - {}'.format(str(chr(letterNumber)), lineNumber, number))

def print_rangoli(size):
    large = ((size - 1) * 4) + 1
    print(large)
    for x in range(size -1, -1, -1):
        #print(str(chr(97 + x)))
        printLine(x, large)
    for x in range(1, size, 1):
        printLine(x, large)


if __name__ == '__main__':
    #n = int(input())
    n = 5
    print_rangoli(n)
    print('{} {} {}'.format(*[1, 2, 3])))


