# >>> The Minion Game
# >>> https://www.hackerrank.com/challenges/the-minion-game/problem

import itertools

def minion_game(string):
    array = []
    for i in range(len(string)):
        els = [''.join(list(x)) for x in itertools.combinations(string, i)]
        array.extend(els)
    print(array)

if __name__ == '__main__':
    s = 'BANANA' #input()
    minion_game(s)