#Mathematics - Number Theory - Constructing a Number

#Manipulating numbers is at the core of a programmer's job. To test how well you know their properties, you are asked to solve the following problem.

#You are given n non-negative integers a1, a2, ..., an. You want to know whether it's possible to construct a new integer using all the digits of these 
#numbers such that it would be divisible by 3. You can reorder the digits as you want. The resulting number can contain leading zeros.

#For example, consider the numbers 50, 40, 90 from which you have to construct a new integer as described above. Numerous arrangements of digits are 
#possible; but we have illustrated one below.

#Complete the function canConstruct which takes an integer array as input and return "Yes" or "No" based on whether or not the required integer can be formed.

#Input Format

#The first line contains a single integer t denoting the number of queries. The following lines describe the queries.

#Each query is described in two lines. The first of these lines contains a single integer n. The second contains  space-separated integers a1, a2, ..., an.

#Constraints

#1 <= t<= 100
#1 <= n <= 100
#1 <= ai <= 10^9

#Subtasks

#n=1
#1 <= a1 <= 10^6

#For 33.33% of the total score:

#Output Format

#For each query, print a single line containing "Yes" if it's possible to construct such integer and "No" otherwise.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'canConstruct' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY a as parameter.
#

def canConstruct(a):
    # Return "Yes" or "No" denoting whether you can construct the required number.
    
    mySum = 0
    for i in a:
        mySum += i % 3
        
    if (mySum % 3 == 0):
        return "Yes"
    else:
        return "No"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = canConstruct(a)

        fptr.write(result + '\n')

    fptr.close()
	
	