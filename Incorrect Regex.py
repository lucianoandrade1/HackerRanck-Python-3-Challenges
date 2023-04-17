#Hackerrank Incorrect Regex

#Author: Luciano Andrade

#You are given a string S.
#Your task is to find out whether S is a valid regex or not.

#Input Format

#The first line contains integer T, the number of test cases.
#The next T lines contains the string S.

#Constraints

#0 < T < 100

import re

for _ in range(int(input())):
    try:
        re.compile(input())
        valid_regex = True
    except re.error:
        valid_regex = False
    print(valid_regex)
	
	
