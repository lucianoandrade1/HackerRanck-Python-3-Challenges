#Hackerrank Re.start() & Re.end()

#Author: Luciano Andrade

#Task
#You are given a string .
#Your task is to find the indices of the start and end of string k in S.

#Input Format

#The first line contains the string S.
#The second line contains the string k.

#Constraints

#0 < len(S) < 100
#0 < len(k) < len(S)

#Output Format

#Print the tuple in this format: (start _index, end _index).
#If no match is found, print (-1, -1).

import re

S = input()

k = input()

p = re.compile('(?=({0}))'.format(k))
matches = re.finditer(p, S)
matches_positions = [(match.start(), match.start() + len(k) - 1) for match in matches]

if matches_positions:
    print(*matches_positions, sep = "\n")
else:
    print((-1,-1))
	
	
	
