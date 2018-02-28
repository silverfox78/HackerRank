# >>> String Formatting
# >>> https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    sizeBinary = len('{0:b}'.format(number))
    for x in range(number):
        value = x + 1
        decimalText = str(value)
        decimalText = ' '*(sizeBinary - len(decimalText)) + decimalText
        octalText = '{0:o}'.format(value)
        octalText = ' '*(sizeBinary - len(octalText)) + octalText
        hexaText = '{0:x}'.format(value)
        hexaText = ' '*(sizeBinary - len(hexaText)) + hexaText
        binaryText = '{0:b}'.format(value)
        binaryText = ' '*(sizeBinary - len(binaryText)) + binaryText
        print('{} {} {} {}'.format(decimalText, octalText, hexaText.upper(), binaryText))

if __name__ == '__main__':
    n = 1254 #int(raw_input())
    print_formatted(n)
