#Hackerrank Data Structures Linked Lists Insert a Node at the Tail of a Linked List

#Author: Luciano Andrade

#You are given the pointer to the head node of a linked list and an integer to add to the list. Create a new node with the given integer. Insert this node at the tail of the linked list and return the head node of the linked list formed after inserting this new node. The given head pointer may be null, meaning that the initial list is empty.

#Function Description

#Complete the insertNodeAtTail function in the editor below.

#insertNodeAtTail has the following parameters:

#SinglyLinkedListNode pointer head: a reference to the head of a list
#int data: the data value for the node to insert

#Returns

#SinglyLinkedListNode pointer: reference to the head of the modified linked list

#Input Format

#The first line contains an integer n, the number of elements in the linked list.
#The next n lines contain an integer each, the value that needs to be inserted at tail.


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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    if head is None:
        return SinglyLinkedListNode(data)
    aux = head
    while aux.next is not None:
        aux = aux.next
    aux.next = SinglyLinkedListNode(data)
    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
	
	
	
