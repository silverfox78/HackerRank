# >>> Day 24: More Linked Lists
# >>> https://www.hackerrank.com/challenges/30-linked-list-deletion/problem

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

# ----------------------------------------------------------------------------

    # def remove(self, heap, value):
    #     exist = False
        
    #     if heap == None:
    #         return heap
    #     else:
    #         puntero = heap
    #         while(puntero.next != None):
    #             if puntero.data == value and exist == False:
    #                 exist = True
    #             else:
    #                 if puntero.data == value and exist:
    #                     print('Elimina: ' + str(puntero.data))
    #                     puntero = puntero.next
    #             if puntero.next != None:
    #                 puntero = puntero.next
    #     return heap
    
    # def removeDuplicates(self,head):
    #     current = head
    #     while current:
    #         print('Busca: ' + str(current.data))
    #         current = self.remove(current, current.data)
    #         self.display(current)
    #         current = current.next
    #     self.display(head)
  
  

  
    def removeDuplicates(self,head):
        if head == None:
            return head
        cur = head
        while cur.next:
            if cur.data == cur.next.data:
                cur.next = cur.next.next
            if cur.next and cur.data != cur.next.data:
                cur = cur.next
        return head
  



# ----------------------------------------------------------------------------

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 