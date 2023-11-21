
#Mathematics - Fundamentals - Minimum Height Triangle

#Alex is attending a Halloween party with his girlfriend, Silvia. At the party, Silvia spots the corner of an 
#infinite chocolate bar (two dimensional, infinitely long in width and length).

#If the chocolate can be served only as 1 x 1 sized pieces and Alex can cut the chocolate bar exactly K times, 
#what is the maximum number of chocolate pieces Alex can cut and give Silvia?

#Input Format
#The first line contains an integer T, the number of test cases. T lines follow.
#Each line contains an integer K.

#Output Format
#T lines; each line should contain an integer that denotes the maximum number of pieces that can be obtained 
#for each test case.

#Constraints

#1<= T <=10
#2 <= K <= 10^7

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'halloweenParty' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER k as parameter.
#

def halloweenParty(k):
    # Write your code here
    
    return round(k / 2) * (k - round(k / 2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        k = int(input().strip())

        result = halloweenParty(k)

        fptr.write(str(result) + '\n')

    fptr.close()