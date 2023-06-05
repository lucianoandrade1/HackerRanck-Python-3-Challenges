#Author: Luciano Andrade

#Mathematics - Fundamentals - Maximum Draws

#A person is getting ready to leave and needs a pair of matching socks. If there are  colors of 
#socks in the drawer, how many socks need to be removed to be certain of having a matching pair?


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def maximumDraws(n):
    # Write your code here
    return n + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = maximumDraws(n)

        fptr.write(str(result) + '\n')

    fptr.close()
	
	
	