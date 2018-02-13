# >>> Find the Runner-Up Score!
# >>> https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = 5 #int(input())
    arr = '2 3 6 6 5'.split() #map(int, input().split())
    
    arregloLimpio = sorted(set(arr), reverse=True)
    print(arregloLimpio[1])