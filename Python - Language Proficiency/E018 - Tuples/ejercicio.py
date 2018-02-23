# >>> Tuples
# >>> https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = 3 #int(input())
    integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] #map(int, input().split())
    arrayList = []
    for elem in integer_list:
        arrayList.append(elem)
    sizeList = len(arrayList)
    for x in range(0, sizeList, n):
        subArray = tuple(arrayList[x:x + n])
        print(hash(subArray))