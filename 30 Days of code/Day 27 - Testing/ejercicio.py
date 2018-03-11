# >>> Day 27: Testing
# >>> https://www.hackerrank.com/challenges/30-testing/problem

#!/bin/python3
import sys
class Test:
    def __init__(self, n, k, a): 
        self.n = n
        self.k = k
        self.a = a
    
    def printTest(self):
        print("{} {}".format(self.n, self.k))
        print(" ".join(map(str, self.a)))

class Cases:
    def __init__(self, t):
        self.t = t
        self.array = []

    def addTest(self, n, k, a):
        self.array.append(Test(n, k, a))

    def printCase(self):
        print(self.t)
        for x in range(self.t):
            self.array[x].printTest()

if __name__ == "__main__":
    case = Cases(5)
    case.addTest(4, 3, [-1, 0, 4, 2])
    case.addTest(5, 2, [0, -1, 2, 1, 4])
    case.addTest(7, 6, [2, 0, -1, 1, 1, 1, 1])
    case.addTest(3, 1, [-1, 0, 4])
    case.addTest(6, 4, [0, -1, 1, 4, 5, 6])
    case.printCase()