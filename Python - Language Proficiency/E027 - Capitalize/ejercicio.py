# >>> Capitalize
# >>> https://www.hackerrank.com/challenges/capitalize/problem

def capitalize(string):
    return ' '.join([x.capitalize() for x in string.split(' ')])

if __name__ == '__main__':
    string = 'chris alan' #input()
    capitalized_string = capitalize(string)
    print(capitalized_string)