# >>> Day 9: Recursion
# >>> https://www.hackerrank.com/challenges/30-recursion/problem

#!/bin/python3
import sys

def factorial(n):
    return 1 if n == 1 else (n * factorial(n - 1))

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
