#Luciano Andrade

#Data Structures Arrays 2D Array

#Given a 6x6 2D Array, arr:

#1 1 1 0 0 0
#0 1 0 0 0 0
#1 1 1 0 0 0
#0 0 0 0 0 0
#0 0 0 0 0 0
#0 0 0 0 0 0

#An hourglass in  is a subset of values with indices falling in this pattern in 's graphical 
#representation:

#a b c
#  d
#e f g

#There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. Calculate the 
#hourglass sum for every hourglass in arr, then print the maximum hourglass sum. The array will 
#always be 6x6.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    
    aux = [[1,1,1],
           [0,1,0],
           [1,1,1]]
    
    s = []
    l=0
    while l<=3:
        k=0
        while k<=3:
            zeros = [[0] * 6 for _ in range(6)]               
            for i1 ,i2 in zip(range(3), range(l,l+3)):
                for j1, j2 in zip(range(3), range(k,k+3)):    
                    zeros[i2][j2] = zeros[i2][j2] + aux[i1][j1]                    
            k=k+1
            result = [[a*b for a, b in zip(i, j)] for i, j in zip(zeros, arr)]
            s.append(sum(map(sum, result)))
        l=l+1  
        
           
    return max(s)
           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
	
	
