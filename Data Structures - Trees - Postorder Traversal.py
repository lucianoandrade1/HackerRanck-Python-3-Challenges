#Author: Luciano Andrade

#Data Structures - Trees - Tree: Postorder Traversal

#Complete the posOrder function in the editor below. It received  parameter: a pointer to the root of 
#a binary tree. It must print the values in the tree's postorder traversal as a single line of 
#space-separated values.

#Input Format

#Our test code passes the root node of a binary tree to the postOrder function.

#Constraints

#1 <= Nodes in the tree <= 500  

#Output Format

#Print the tree's postorder traversal as a single line of space-separated values.

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def postOrder(root):
    #Write your code here
    if root is None:
        return
 
    # First recur on left child
    postOrder(root.left)
 
    # the recur on right child
    postOrder(root.right)
 
    # now print the data of node
    print(root.info, end=" ")


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

postOrder(tree.root)


