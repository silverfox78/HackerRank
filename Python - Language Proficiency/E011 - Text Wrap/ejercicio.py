# >>> Text Wrap
# >>> https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    #string, max_width = input(), int(input())
    string = "In my project, I have a bunch of strings that are read in from a file. Most of them, when printed in the command console, exceed 80 characters in length and wrap around, looking ugly."
    max_width = 3
    result = wrap(string, max_width)
    print(result)