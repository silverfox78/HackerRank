# >>> Kangaroo
# >>> https://www.hackerrank.com/challenges/kangaroo/problem

#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    if(v2>=v1):
        return 'NO'
    else:
        return 'NO' if ((x2-x1)%(v1-v2)!=0) else 'YES'
    


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)