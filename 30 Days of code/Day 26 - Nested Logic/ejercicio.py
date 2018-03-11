# >>> Day 26: Nested Logic
# >>> https://www.hackerrank.com/challenges/30-nested-logic/problem

#!/bin/python3
import sys


if __name__ == "__main__":
    date01 = list(map(int, input().strip().split(' ')))
    date02 = list(map(int, input().strip().split(' ')))   

    if date01[2] > date02[2]:
        print(10000)
    else:
        if date01[1] > date02[1] and date01[2] == date02[2]:
            print(500 * abs(date01[1] - date02[1]))
        else:
            if date01[0] > date02[0] and date01[1] == date02[1] and date01[2] == date02[2]:
                print(15 * abs(date01[0] - date02[0]))
            else:
                print(0)
