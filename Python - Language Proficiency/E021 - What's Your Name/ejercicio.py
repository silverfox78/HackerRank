# >>> What's Your Name?
# >>> https://www.hackerrank.com/challenges/whats-your-name/problem

def print_full_name(a, b):
    text = "Hello {} {}! You just delved into python."
    print(text.format(a.strip(), b.strip()))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)