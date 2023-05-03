#Author: Luciano Andrade

#Data Structures - Trees - Tree: Height of a Binary Tree

#The height of a binary tree is the number of edges between the tree's root and its furthest 
#leaf. For example, the following binary tree is of height 2:

#Function Description

#Complete the getHeight or height function in the editor. It must return the height of a binary 
#tree as an integer.

#getHeight or height has the following parameter(s):

# - root: a reference to the root of a binary tree.
 
#Note -The Height of binary tree with single node is taken as zero.

#Input Format

#The first line contains an integer n, the number of nodes in the tree.
#Next line contains n space separated integer where th integer denotes node[i].data.

#Note: Node values are inserted into a binary search tree before a reference to the tree's root node is passed to your function. In a binary search tree, all nodes on the left branch of a node are less than the node value. All values on the right branch are greater than the node value.

#Constraints

#1<= node.data[i] <= 20
#1 <= n <= 20

#Output Format

#Your function should return a single integer denoting the height of the binary tree.


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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):

    if root is None:
        return -1
 
    # Compute the depth of each subtree
    lheight = height(root.left)
    rheight = height(root.right)
 
    return max(lheight, rheight) + 1
                    


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))


