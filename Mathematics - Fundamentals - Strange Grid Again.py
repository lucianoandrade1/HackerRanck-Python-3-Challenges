
#Mathematics - Fundamentals - Strange Grid Again

#A strange grid has been recovered from an old book. It has 5 columns and infinite number of rows. 
#The bottom row is considered as the first row. First few rows of the grid are like this:

#..............

#..............

#20 22 24 26 28

#11 13 15 17 19

#10 12 14 16 18

# 1  3  5  7  9

# 0  2  4  6  8
 
#The grid grows upwards forever!

#Your task is to find the integer in th column in th row of the grid.

#Input Format

#There will be two integers r and c separated by a single space.

#Constraints

#1 <= r <= 2*10^9
#1 <= c <= 5

#Rows are indexed from bottom to top and columns are indexed from left to right.

#Output Format

#Output the answer in a single line.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeGrid' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER r
#  2. INTEGER c
#

def strangeGrid(r, c):
    # Write your code here
    
    i = (math.ceil(r / 2) - 1) * 5 + c - 1
    
    if r % 2 == 0.0:
        return i * 2 + 1
    if r % 2 != 0.0:
        return i * 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()
	
	
	