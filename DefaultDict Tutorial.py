#Hackerrank Alphabet Rangoli

#Author: Luciano Andrade

#In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. 
#There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. 
#Print the indices of each occurrence of m in group A. If it does not appear, print -1.

#Example


#Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

#For the first word in group B, 'a', it appears at positions 1 and 3 in group A. The second word, 'c', does not appear in group A, so print -1.

#Expected output:

#1 3
#-1

#Input Format

#The first line contains integers, n and m separated by a space.
#The next  lines contains the words belonging to group A.
#The next  lines contains the words belonging to group B.

#Constraints
#1 <= n <= 10000
#1 <= m <= 100
#1 <= length of each word in the inout <= 100

#Output Format

#Output m lines.
#The ith line should contain the 1-indexed positions of the occurrences of the ith word separated by spaces.

from collections import defaultdict

d = defaultdict(list)

m, n = map(int, input().split())

for _ in range(m):
    d['A'].append(input())
    
for _ in range(n):
    d['B'].append(input())
    
    
for B in d['B']:
    
    l = [i+1 for i, val in enumerate(d['A']) if val==B]
    
    if not l: 
        print(-1) 
    else:
        print(' '.join(map(str, l)))
		
		
		
