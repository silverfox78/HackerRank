# >>> Write a function
# >>> https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    if year >= 1900:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                return False
            return True
    return False

year = 1900
print(is_leap(year))
year = 1990
print(is_leap(year))
year = 2016
print(is_leap(year))
year = 2000
print(is_leap(year))
year = 2200
print(is_leap(year))