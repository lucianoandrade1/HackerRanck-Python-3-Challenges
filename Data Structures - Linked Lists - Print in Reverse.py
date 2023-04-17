#Author: Luciano Andrade

#Data Structures - Linked Lists - Print in Reverse

#Given a pointer to the head of a singly-linked list, print each  value from the reversed 
#list. If the given list is empty, do not print anything.

#Example

#head* refers to the linked list with data values 1->2->3->->NULL

#Print the following:
#3
#2
#1

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

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

#
# Complete the 'reversePrint' function below.
#
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(llist):
    prev = None
    current = llist
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    llist = prev
    return llist
        
def reversePrint(llist):
    # Write your code here
    temp = reverse(llist)
    while(temp):
        print(temp.data)
        temp = temp.next    
    

if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        reversePrint(llist.head)



