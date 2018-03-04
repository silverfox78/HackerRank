# >>> Day 25: Running Time and Complexity
# >>> https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

#!/bin/python3
import sys
import math

def isPrime(value):
    if value == 1:
        return False
    if value <= 3:
        return True
    answer = False
    count = 2
    maximum = int(math.sqrt(value))
    while not answer:
        if value % count == 0:
            answer = True
        count += 1
        if count > maximum:
            break;
    return not answer

if __name__ == "__main__":
    T=int(input())
    for i in range(T):
        n=int(input())
        print('Prime' if isPrime(n) else 'Not prime')