#Python - Numpy - Linear Algebra

#Author: Luciano Andrade

#Task

#You are given a square matrix A with dimensions N X N. Your task is to find the determinant. 
#Note: Round the answer to 2 places after the decimal.

#Input Format

#The first line contains the integer N.
#The next N lines contains the N space separated elements of array A.

#Output Format

#Print the determinant of A.

import numpy

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(float, input().split(" "))))

print (round(numpy.linalg.det(l),2))