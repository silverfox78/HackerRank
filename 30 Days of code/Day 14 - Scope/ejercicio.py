## >>> Day 14 - Scope
## >>> https://www.hackerrank.com/challenges/30-scope/problem

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
	# Add your code here

    def computeDifference(self):
        arr = sorted(self.__elements)
        largo = len(arr)
        self.maximumDifference = 0 if largo == 0 else abs(arr[largo - 1] - arr[0])

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)