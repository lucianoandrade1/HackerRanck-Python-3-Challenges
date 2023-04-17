#Algorithms - Warmup - Time Conversion

#Author: Luciano Andrade

#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

#Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
#- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    h = s.split(":")
    
    hour = int(h[0])
    minutes = int(h[1])
    
    if "AM" in h[2]:
        seconds = h[2].replace("AM","")
        if hour == 12: hour = 0
    
    if "PM" in h[2]:
        seconds = h[2].replace("PM","")
        if hour != 12: hour += 12
        
    return str(hour).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()


