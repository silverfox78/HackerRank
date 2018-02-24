# >>> Mutations
# >>> https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    chain = list(string.strip())
    size = len(chain)
    if position > size:
        return string
    chain[position] = character
    return ''.join(chain)

if __name__ == '__main__':
    # s = input()
    # i, c = input().split()
    s = 'abracadabra'
    i = 5
    c = 'k'
    s_new = mutate_string(s, int(i), c)
    print(s_new)