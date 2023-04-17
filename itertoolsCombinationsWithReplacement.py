#Hackerrank itertools.combinations_with_replacement()

#Author: Luciano Andrade

#Task

#You are given a string S.

#Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

#Input Format

#A single line containing the string S and integer value k separated by a space.

#Constraints

#0 < k <= len(S)

#The string contains only UPPERCASE characters.

#Output Format

#Print the combinations with their replacements of string S on separate lines.

from itertools import combinations_with_replacement

s, N = input().split()

l = list(combinations_with_replacement(s,int(N)))

print('\n'.join(sorted([''.join(sorted(tup)) for tup in l])))


