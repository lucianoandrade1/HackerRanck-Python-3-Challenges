#Hackerrank Validating phone numbers

#Author: Luciano Andrade

#Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.

#A valid mobile number is a ten digit number starting with 7 a 8 or 9.

#Concept

#A valid mobile number is a ten digit number starting with 7 a 8 or 9.

#Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python.

#https://developers.google.com/edu/python/regular-expressions

#Input Format

#The first line contains an integer N, the number of inputs.
#N lines follow, each containing some string.

#Constraints

#1 <= N <= 10
#2 <= len(Number) <= 15

#Output Format

#For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

import re
N = int(input())

for _ in range(N):
    
    number = input()
    
    print("YES" if re.findall(r'^\s*[7-9]\d{9}\s*$',number) else "NO")
	
