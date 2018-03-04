# >>> Day 23: BST Level-Order Traversal
# >>> https://www.hackerrank.com/challenges/30-binary-trees/problem

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root


# ----------------------------------------------------------------------------

    def countLeavel(self, node, size):
        maximo = size
        if node.left == None and node.right == None:
            return maximo
        else:
            if node.left != None:
                izq = self.countLeavel(node.left, size + 1)
                if izq > maximo:
                    maximo = izq
            if node.right != None:
                der = self.countLeavel(node.right, size + 1)
                if der > maximo:
                    maximo = der
        return maximo

    def printLeavel(self, node, vector, busca, nivel):
        array = vector
        if busca == nivel:
            if node.left != None:
                array.append(node.left.data)
            if node.right != None:
                array.append(node.right.data)

        if node.left != None:
            array = self.printLeavel(node.left, array, busca, nivel + 1)
        if node.right != None:
            array = self.printLeavel(node.right, array, busca, nivel + 1)
        return array

    def levelOrder(self,root):
        size = 0
        salida = ''
        if root != None:
            size = self.countLeavel(root, size)

        if root != None:
            for x in range(size + 1):
                array = []
                if x == 0:
                    array.append(root.data)
                else:
                    array = self.printLeavel(root, array, x, 1)
            salida += ' ' + ' '.join([str(x) for x in array])
        print(salida.strip())

# ----------------------------------------------------------------------------

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)


# 25 12 39 9 19 23 31 55 35 41 60 70 90
# 25 12 39 9 19 31 55 23 35 41 60 70 90
# 25 12 39 9 19 31 55 23 35 41 60 70 90

