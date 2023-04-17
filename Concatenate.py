#Hackerrank Concatenate

#Author: Luciano Andrade

#Task

#You are given two integer arrays of size NxP and MxP (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.

#Input Format

#The first line contains space separated integers N, M and P.
#The next N lines contains the space separated elements of the P columns.
#After that, the next M lines contains the space separated elements of the P columns.

#Output Format

#Print the concatenated array of size (N + M) x P.

import numpy

N, M, P = map(int, input().split())

arr1 = numpy.empty(shape=[0, P], dtype=int)
arr2 = numpy.empty(shape=[0, P], dtype=int)

for _ in range(N):
    arr1 = numpy.append(arr1,[list(map(int, input().split()))], axis = 0)
    
for _ in range(M):
    arr2 = numpy.append(arr2, [list(map(int, input().split()))], axis = 0)

print(numpy.concatenate((arr1, arr2), axis = 0))

