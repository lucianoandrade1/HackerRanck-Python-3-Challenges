#Author: Luciano Andrade

#Data Structures - Linked Lists - Get Node Value

#Given a pointer to the head of a linked list and a specific position, determine the data 
#value at that position. Count backwards from the tail node. The tail is at postion 0, its 
#parent is at 1 and so on.

#Example

#head refers to 3->2->1->0->NULL
#positionFromTail=2

#Each of the data values matches its distance from the tail. The value 2 is at the desired 
#position.

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'getNode' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER positionFromTail
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def getNode(llist, positionFromTail):
    # Write your code here
    temp = llist
  
    length = 0
    while temp is not None:
        temp = temp.next
        length += 1
  
    if positionFromTail > length:
        return
    
    temp = llist
    for i in range(0, length - positionFromTail - 1):
        temp = temp.next
        
    return temp.data
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = getNode(llist.head, position)

        fptr.write(str(result) + '\n')

    fptr.close()
	
	
	
	