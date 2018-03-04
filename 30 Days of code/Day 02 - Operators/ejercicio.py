# >>>Day 2: Operators
# >>> https://www.hackerrank.com/challenges/30-operators/problem
#!/bin/python3

import sys

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    valorTip = float((meal_cost * (0 if tip_percent is None else tip_percent/100)))
    valorTax = float((meal_cost * (0 if tax_percent is None else tax_percent/100)))
    total = round(meal_cost + valorTip + valorTax)
    print('The total meal cost is ' + str(total) + ' dollars.')