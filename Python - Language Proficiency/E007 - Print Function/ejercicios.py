# >>> Print Function
# >>> https://www.hackerrank.com/challenges/python-print/problem
if __name__ == '__main__':
    n = 3
    if n > 0:
        texto = ''
        for i in range(n):
            texto += str(i+1)
        print(texto)