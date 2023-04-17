#Hackerrank Capitalize!
#Author: Luciano Andrade

#Task
#You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 

#For example, alison heck should be capitalised correctly as Alison Heck.

#Given a full name, your task is to capitalize the name appropriately.

#Input Format

#A single line of input containing the full name, .

#Constraints

#The string consists of alphanumeric characters and spaces.
#Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.



import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    
    l = re.split(r'(\s+)', s)
    
    sAux = ""
    
    for n in l:
        sAux = sAux + n.capitalize()
        
    return sAux
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
