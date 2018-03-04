# >>> Grading Students
# >>> https://www.hackerrank.com/challenges/grading/problem

#!/bin/python3

import sys

def solve(grades):
    array = []
    for x in grades:
        decimal = int(x / 10) * 10
        diference = x - decimal
        add = 5 if diference < 5 else 10
        evalvalue = decimal + add
        diferenceFinal = evalvalue - x
        if diferenceFinal < 3:
            evalvalueFinal = evalvalue if evalvalue >= 40 else x
        else:
            evalvalueFinal = x
        array.append(evalvalueFinal)
    return array

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
