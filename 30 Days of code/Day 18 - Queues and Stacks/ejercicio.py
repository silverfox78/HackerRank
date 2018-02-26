# >>> Day 18: Queues and Stacks
# >>> https://www.hackerrank.com/challenges/30-queues-stacks/problem


import sys

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []
    
    #STACK
    def pushCharacter(self, ch):
        self.stack.append(ch)

    #QUEUE
    def enqueueCharacter(self, ch):
        self.stack.append(ch)

    #STACK
    def popCharacter(self):
        size = len(self.stack)
        if size > 0:
            return self.stack.pop(size - 1)
        return None

    #QUEUE
    def dequeueCharacter(self):
        size = len(self.stack)
        if size > 0:
            return self.stack.pop(0)
        return None

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")  