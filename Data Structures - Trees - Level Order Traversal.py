#Author: Luciano Andrade

#Data Structures - Trees - Level Order Traversal

#Given a pointer to the root of a binary tree, you need to print the level order traversal of 
#this tree. In level-order traversal, nodes are visited level by level from left to right. 
#Complete the function  and print the values in a single line separated by a space.

#For example:

#     1
#      \
#       2
#        \
#         5
#        /  \
#       3    6
#        \
#         4  

#For the above tree, the level order traversal is .

#1->2->5->3->6->4

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
def levelOrder(root):
    #Write your code here
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)
 
# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.info, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)
  
 
def height(node):
    
    if node is None:
        return 0
    
    # Compute the height of each subtree
    lheight = height(node.left)
    rheight = height(node.right)
 
    return max(lheight, rheight) + 1 


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)

