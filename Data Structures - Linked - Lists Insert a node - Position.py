#Author: Luciano Andrade

#Data Structures - Linked - Lists Insert a node at a specific position in a linked list

#Given the pointer to the head node of a linked list and an integer to insert at a certain 
#position, create a new node with the given integer as its data attribute, insert this node at 
#the desired position and return the head node.

#A position of 0 indicates head, a position of 1 indicates one node away from the head and 
#so on. The head pointer given may be null meaning that the initial list is empty.

#Example
# refers to the first node in the list 1->2->3

#data=4

position=2

#Insert a node at position 2 with data=4. The new list is 1->2->4->3


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
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    # Write your code here

    newNode = SinglyLinkedListNode(data) 
    if(position < 1):
      print("\nposition should be >= 1.")
    elif (position == 1):
      newNode.next = llist
      llist = newNode
    else:    
      temp = llist
      for i in range(1, position):
        if(temp != None):
          temp = temp.next   
      if(temp != None):
        newNode.next = temp.next
        temp.next = newNode  
      else:
        print("\nThe previous node is null.")    
    
    return llist
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()



