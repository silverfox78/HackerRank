# >>> Day 15: Linked List
# >>> https://www.hackerrank.com/challenges/30-linked-list/problem

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

# --------------------------------------------------------------------------

    def insert(self,head,data): 
        if head is None:
            return Node(data)
        else:
            puntero = head
            while True:
                if puntero.next is None:
                    puntero.next = Node(data)
                    break
                else:
                    puntero = puntero.next
            return head

# --------------------------------------------------------------------------

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 