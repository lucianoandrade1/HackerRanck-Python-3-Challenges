#Author: Luciano Andrade

#Data StructuresLinked ListsInsert a node at the head of a linked list

#Given a pointer to the head of a linked list, insert a new node before the head. The next value 
#in the new node should point to head and the data value should be replaced with a given value. Return 
#a reference to the new head of the list. The head pointer given may be null meaning that the 
#initial list is empty.

#Function Description

#Complete the function insertNodeAtHead in the editor below.

#insertNodeAtHead has the following parameter(s):

# - SinglyLinkedListNode llist: a reference to the head of a list
# - data: the value to insert in the data field of the new node

#Input Format

#The first line contains an integer n, the number of elements to be inserted at the head of the list.
#The next n lines contain an integer each, the elements to be inserted, one per function call.

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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtHead(llist, data):
    # Write your code here
    new_node = SinglyLinkedListNode(data)
    new_node.next = llist
    
    return new_node
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    
    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')
    
    fptr.close()
	
	
