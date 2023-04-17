#Author:Luciano Andrade

#Data Structures - Linked Lists - Merge two sorted linked lists

#Given pointers to the heads of two sorted linked lists, merge them into a single, sorted 
#linked list. Either head pointer may be null meaning that the corresponding list is empty.

#Example
#headA refers to 1->3->7->NULL
#headB refers to 1->2->NULL

#The new list is 1->1->2->3->7->NULL

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

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    
    head_ptr = temp_ptr = SinglyLinkedListNode(None)
    
    while head1 or head2:
        if head1 and (not head2 or head1.data <= head2.data):
            temp_ptr.next = SinglyLinkedListNode(head1.data)
            head1 = head1.next
        else:
            temp_ptr.next = SinglyLinkedListNode(head2.data)
            head2 = head2.next
        temp_ptr = temp_ptr.next
    return head_ptr.next    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()

