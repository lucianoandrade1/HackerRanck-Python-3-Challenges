#Algorithms Implementation Number Line Jumps

#Author: Luciano Andrade

#You are choreographing a circus show with various animals. For one act, you are given two 
#kangaroos on a number line ready to jump in the positive direction (i.e, toward positive 
#infinity).

#The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
#The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
#You have to figure out a way to get both kangaroos at the same location at the same time 
#as part of the show. If it is possible, return YES, otherwise return NO.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    
    return "YES" if (v2!=v1) and (x2-x1)%(v2-v1)==0 and x2-x1>0 and v1-v2>0 else "NO"
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
	
	