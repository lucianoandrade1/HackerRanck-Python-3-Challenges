#Algorithms - Implementation - Grading Students

#Author: Luciano Andrade

#HackerLand University has the following grading policy:

#-Every student receives a grade in the inclusive range from 0 to 100.
#-Any grade less than 40 is a failing grade.

#Sam is a professor at the university and likes to round each student's grade according to these rules:

#-If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
#-If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def findNextMultipleOf5(n):
    
    m = n
    while True:
        m += 1
        if m % 5 == 0:
            break
            
    return m

def gradingStudents(grades):
    # Write your code here
    ng = []
 
    for g in grades:
        n5 = findNextMultipleOf5(g)
        if n5 - g < 3 and g >= 38:
            ng.append(n5)
        else: ng.append(g)
        
    return ng    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



