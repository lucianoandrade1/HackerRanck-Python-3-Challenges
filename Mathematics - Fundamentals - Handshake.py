

#Author: Luciano Andrade

#Mathematics - Fundamentals - Handshake

#At the annual meeting of Board of Directors of Acme Inc. If everyone attending shakes hands 
#exactly one time with every other attendee, how many handshakes are there?



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'handshake' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def handshake(n):
    # Write your code here
    return math.comb(n, 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()
	
	
	