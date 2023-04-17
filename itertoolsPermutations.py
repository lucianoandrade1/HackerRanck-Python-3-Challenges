#Hackerrank itertools.permutations(iterable[, r])

#Author: Luciano Andrade

#This tool returns successive  length permutations of elements in an iterable.

#If  is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.

#Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

#Task

#You are given a string S.
#Your task is to print all possible permutations of size K of the string in lexicographic sorted order.

#Input Format

#A single line containing the space separated string S and the integer value K.

#Constraints

#0 < k < len(S)

#The string contains only UPPERCASE characters.

#Output Format

#Print the permutations of the string S on separate lines.


import itertools

if __name__ == '__main__':
    
    a = input().split()
    
    s = sorted(set(list(a[0])))
    n = int(a[-1])

    l = list(itertools.permutations(s, r=n))
    
    m = len(l)
    
    print("\n".join(["".join([l[row][column] for column in range(n)]) for row in range(m)]))
	
	
