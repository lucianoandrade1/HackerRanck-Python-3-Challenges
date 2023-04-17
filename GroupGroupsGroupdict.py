#Hackerrank Group(), Groups() & Groupdict()

#Author: Luciano Andrade

#Task

#You are given a string S.
#Your task is to find the first occurrence of an alphanumeric character in S (read from left to right) that has consecutive repetitions.

#Input Format

#A single line of input containing the string S.

#Constraints

#0 < len(S) < 100

#Output Format

#Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

import re
m = re.findall(r'([a-zA-Z0-9])\1+?',input())

print(-1 if len(m) == 0 else m[0])

