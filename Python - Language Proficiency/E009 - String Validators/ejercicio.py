# >>> String Validators
# >>> https://www.hackerrank.com/challenges/string-validators/problem

# str.isalnum() - In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
# str.isalpha() - In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
# str.isdigit() - In the third line, print True if  has any digits. Otherwise, print False. 
# str.islower() - In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
# str.isupper() - In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

if __name__ == '__main__':
    s = 'qA2' #input()
    isalnum = isalpha = isdigit = islower = isupper = False
    for elem in s:
        if not isalnum:
            isalnum = elem.isalnum()
        if not isalpha:
            isalpha = elem.isalpha()
        if not isdigit:
            isdigit = elem.isdigit()
        if not islower:
            islower = elem.islower()
        if not isupper:
            isupper = elem.isupper()
        if isalnum and isalpha and isdigit and islower and isupper:
            break
    print(isalnum)
    print(isalpha)
    print(isdigit)
    print(islower)
    print(isupper)