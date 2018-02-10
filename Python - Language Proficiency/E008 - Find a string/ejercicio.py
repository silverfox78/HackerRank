# >>> Find a string
# >>> https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    largoString = len(string)
    largoSubString = len(sub_string)
    contador = 0
    for i in range(largoString):
        contador += 1 if string[i:i + largoSubString] == sub_string else 0
    return contador
    
if __name__ == '__main__':
    string = 'ABCDCDC' #input().strip()
    sub_string = 'CDC' #input().strip()
    
    count = count_substring(string, sub_string)
    print(count)