# >>> Apple and Orange
# >>> https://www.hackerrank.com/challenges/apple-and-orange/problem


#!/bin/python3

import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    #print('s:{} - t:{} - a:{} - b:{} - apples:{} - oranges:{}'.format(s, t, a, b, apples, oranges))
    countApples = 0
    countOrange = 0
    for x in apples:
        if s <= (a + x) <= t:
            countApples += 1
    for x in oranges:
        if s <= (b + x) <= t:
            countOrange += 1
    print('{}\n{}'.format(countApples, countOrange))

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    countApplesAndOranges(s, t, a, b, apple, orange)