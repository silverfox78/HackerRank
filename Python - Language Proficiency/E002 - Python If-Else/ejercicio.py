# >>> Python If-Else
# >>> https://www.hackerrank.com/challenges/py-if-else/problem
if __name__ == '__main__':
    n = int(input())
    if n % 2 != 0 or (n >= 6 and n <= 20 and n % 2 == 0):
        print('Weird')
    else:
        print('Not Weird')