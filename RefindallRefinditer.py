#Hackerrank Re.findall() & Re.finditer()

#Author: Luciano Andrade

#Task
#You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
#Your task is to find all the substrings of S that contains 2 or more vowels.
#Also, these substrings must lie in between 2 consonants and should contain vowels only.

#Note :
#Vowels are defined as: AEIOU and aeiou.
#Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

#Input Format

#A single line of input containing string S.

#Constraints

#0 < len(S) < 100

#Output Format

#Print the matched substrings in their order of occurrence on separate lines.
#If no match is found, print -1.

import re
l = re.findall(r"[^aiueo]([aiueoAIUEO]{2,})(?=[^aiueo])", input())

print (-1 if len(l)==0 else '\n'.join(l))

