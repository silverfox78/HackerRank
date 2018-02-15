# >>> Fun Game
# >>> https://www.hackerrank.com/challenges/fun-game-1/problem

#!/bin/python3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = sorted(list(map(int, input().strip().split(' '))), reverse=True)
        b = sorted(list(map(int, input().strip().split(' '))), reverse=True)
        if n == 1:
            print('First')
            break
        largoA = int((n / 2) if n % 2 == 0 else int((n / 2) + 0.5))
        largoB = int(n - largoA)
        jugadorA = sum(int(x) for x in a[:largoA])
        jugadorB = sum(int(x) for x in b[:largoB])
        print('Tie' if jugadorA == jugadorB else ('First' if jugadorA > jugadorB else 'Second'))