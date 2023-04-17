#Hackerrank Alphabet Rangoli

#Author: Luciano Andrade

#Task
#Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

#Input Format

#The first line of input contains an integer, M.
#The second line contains M space-separated integers.
#The third line contains an integer, N.
#The fourth line contains N space-separated integers.

#Output Format

#Output the symmetric difference integers in ascending order, one per line.

M = int(input())

Mlist = set(map(int, input().split()))

N = int(input())

Nlist = set(map(int, input().split()))

print('\n'.join(map(str, sorted(Mlist.difference(Nlist).union(Nlist.difference(Mlist))))))



