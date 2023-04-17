#Author: Luciano Andrade

#Data Structures - Linked Lists - Inserting a Node Into a Sorted Doubly Linked List

#Given a reference to the head of a doubly-linked list and an integer, , create a new 
#DoublyLinkedListNode object having data value  and insert it at the proper location to 
#maintain the sort.

#Example

#head refers to the list 1<->2<->4<->NULL
#data=3

#Return a reference to the new list: 1<->2<->3<->4<->NULL.

#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
    
def sortedInsert(llist, data):
    current=llist
    node=DoublyLinkedListNode(data)
    if current.data>data or current.data==data:
        node.next=current
        current.prev=node
        llist=node
        return llist
    while current.next:
        if (current.data<data and current.next.data>data) or current.data==data:
            node.next=current.next
            current.next.prev=node
            node.prev=current
            current.next=node
            return llist
        current=current.next
    if current.data<data or current.data==data:
        node.prev=current
        current.next=node
        return llist    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
	
	
	