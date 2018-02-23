# >>> sWAP cASE
# >>> https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    return ''.join(list([x.upper() if x.islower() else x.lower() for x in s]))

if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".' #input()
    result = swap_case(s)
    print(result)