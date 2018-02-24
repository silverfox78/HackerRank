# >>> Designer Door Mat
# >>> https://www.hackerrank.com/challenges/designer-door-mat/problem

def writeLine(row, size):
    mark = '.|.' * ((row * 2) - 1)
    scriptSize = int((size - len(mark))/2)
    return '{}{}{}'.format(''.rjust(scriptSize, '-'), mark, ''.ljust(scriptSize, '-'))

def writeWelcome(size):
    word = 'WELCOME'
    scriptSize = int((size - len(word))/2)
    return '{}{}{}'.format(''.rjust(scriptSize, '-'), word, ''.ljust(scriptSize, '-'))

def makeLogo(rows, cols):
    lines = int(rows/2)
    for x in range(lines):
        print(writeLine(x +1, cols))
    print(writeWelcome(cols))
    for x in range(lines, 0, -1):
        print(writeLine(x, cols))

makeLogo(9, 27)

# ---------------------------------------------------------------------------------------------

N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2): 
    print('{}{}{}'.format(''.rjust(int((M - len(('.|.' * i)))/2), '-'), ('.|.' * i), ''.ljust(int((M - len(('.|.' * i)))/2), '-')))
print('{}{}{}'.format(''.rjust(int((M - len('WELCOME'))/2), '-'), 'WELCOME', ''.ljust(int((M - len('WELCOME'))/2), '-')))
for i in range(N-2,-1,-2): 
    print('{}{}{}'.format(''.rjust(int((M - len(('.|.' * i)))/2), '-'), ('.|.' * i), ''.ljust(int((M - len(('.|.' * i)))/2), '-')))
