#Author: Luciano Andrade

#Algorithms Warmup Mini-Max Sum

#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
#Then print the respective minimum and maximum values as a single line of two space-separated long integers.

#Example

#arr = [1,3,5,7,9]

#The minimum sum is 1 + 2 + 5 + 7 = 16 and the maximum sum is 3 + 5 + 7 + 9 = 24. 

#The function prints

#16 24

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def twoPowerNComb(items):

    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        comb = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                comb.append(items[j])
        yield comb

def miniMaxSum(arr):
    # Write your code here

    #in this case it will return the combinations with 4 elements
    n=4
    arrComb = []
    for i in twoPowerNComb(arr):
        if len(i)==n:
            arrComb.append(i)
     
    s = []
    for i in arrComb:
        s.append(sum(i))
            
    return min(s), max(s)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    
    x, y = miniMaxSum(arr) 

    print(x, y)
