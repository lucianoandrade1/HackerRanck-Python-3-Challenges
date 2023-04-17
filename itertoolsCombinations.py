#Hackerrank itertools.combinations()

#Author: Luciano Andrade

#Task

#You are given a string S.

#Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

#Input Format

#A single line containing the string S and integer value k separated by a space.

#Constraints

#0 < k <= len(S)

#The string contains only UPPERCASE characters.

#Output Format

#Print the different combinations of string S on separate lines.

from itertools import combinations

s, N = input().split()

l1 = list()
l2 = list()
for i in range(int(N)):
    l1.append(list(combinations(s,int(i+1))))
    
l2 = [''.join(sorted(tups)) for s in l1 for tups in s]

print('\n'.join(map(str, sorted(sorted(l2), key=len))))


