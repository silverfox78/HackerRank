# >>> Time Conversion
# >>> https://www.hackerrank.com/challenges/time-conversion/problem

#!/bin/python3

import sys

def timeConversion(s):
    hour = s[0:2]
    minute = s[3:5]
    second = s[6:8]
    time = s[8:].upper()
    if time == 'PM':
        if hour == '00' and minute == '00' and second == '00':
            return '24:00:00'
        if int(hour) < 12:
            hour = '{0:02d}'.format(int(hour) + 12)
    else:
        if hour == '12':
            hour = '00'
    return '{}:{}:{}'.format(hour, minute, second)

s = '12:45:54PM' #input().strip()
result = timeConversion(s)
print(result)
