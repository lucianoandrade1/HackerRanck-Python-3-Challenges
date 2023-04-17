#Hackerrank Check Strict Superset

#Author: Luciano Andrade

#You are given a set A and n other sets.
#Your job is to find whether set A is a strict superset of each of the N sets.

#Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

#A strict superset has at least one element that does not exist in its subset.

#Example
#Set([1,3,4]) is a strict superset of set([1,3]).
#Set([1,3,4]) is not a strict superset of set([1,3,4]).
#Set([1,3,4]) is not a strict superset of set([1,3,5]).

#Input Format

#The first line contains the space separated elements of set A.
#The second line contains integer n, the number of other sets.
#The next n lines contains the space separated elements of the other sets.

#Constraints

#0 < len(set(A)) < 501
#0 < N < 21
#0 < len(otherSets) < 101

#Output Format

#Print True if set A is a strict superset of all other N sets. Otherwise, print False.

A = set(map(int,input().split()))

n = int(input())

check = True
for _ in range(n):
    B = set(map(int,input().split()))
    if not A.issuperset(B):
        check = False
        break
        
print(check)


