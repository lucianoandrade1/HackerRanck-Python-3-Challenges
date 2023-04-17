#Author: Luciano Andrade

#Data Structures - Linked Lists - Delete a Node

#Delete the node at a given position in a linked list and return a reference to the head 
#node. The head is at position 0. The list may be empty after you delete the node. In that 
#case, return a null value.

#Example

#llist = 0 -> 1 -> 2 -> 3
#position=2

#After removing the node at position 2, llist = 0 -> 1 -> 3.

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
# Complete the 'deleteNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(llist, position):
    # Write your code here
    temp = llist
    prev = llist
    for i in range(0, position + 1):
        if i == 0 and position == 0:
            llist = llist.next
        else:
            if i == position and temp is not None:
                prev.next = temp.next
            else:
                prev = temp
                # Position was greater than
                # number of nodes in the list
                if prev is None:
                    break
                temp = temp.next
    return llist    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')

    fptr.close()



