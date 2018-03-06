# >>> Day 26: Nested Logic
# >>> https://www.hackerrank.com/challenges/30-nested-logic/problem

#!/bin/python3

from datetime import date, time, datetime
import sys


if __name__ == "__main__":
    date01 = list(map(int, input().strip().split(' ')))
    date02 = list(map(int, input().strip().split(' ')))
    realdate01 = datetime.strptime('{}-{}-{}'.format(date01[2], date01[1], date01[0]), '%Y-%m-%d')
    realdate02 = datetime.strptime('{}-{}-{}'.format(date02[2], date02[1], date02[0]), '%Y-%m-%d')
    delta = realdate01 - realdate02
    days = delta.days

    if days <= 0:
        print(0)
    else:
        if date01[2] == date02[2] and date01[1] == date02[1]:
            print(days * 15)
        else:
            if date01[2] == date02[2]:
                print(500 * abs(date01[1] - date02[1]))
            else:   
                print(10000)