#Mars Exploration
#!/bin/python3
from itertools import repeat
import sys

def marsExploration(s):
    esperado = ''.join(list(repeat('SOS',int(len(s)/3))))
    return sum(s[i]!=esperado[i] for i in range(len(s)))

if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)