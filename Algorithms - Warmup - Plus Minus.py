#Algorithms Warmup Plus Minus

#Author: Luciano Andrade

#Given an array of integers, calculate the ratios of its elements that are positive, 
#negative, and zero. Print the decimal value of each fraction on a new line with  
#places after the decimal.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    
    p=0
    z=0
    n=0
    for i in arr:
        if i > 0:
            p+=1
        if i < 0:
            n+=1
        if i==0:
            z+=1

    print("%.6f" % (p / len(arr)))
    print("%.6f" % (n / len(arr)))
    print("%.6f" % (z / len(arr)))
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


