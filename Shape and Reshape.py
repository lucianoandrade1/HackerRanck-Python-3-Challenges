#Hackerrank Shape and Reshape

#Author: Luciano Andrade

#Task

#You are given a space separated list of nine integers. Your task is to convert this list into a 3x3 NumPy array.

#Input Format

#A single line of input containing 9 space separated integers.

#Output Format

#Print the 3x3 NumPy array.

import numpy

arr = numpy.array(list(map(int, input().split())))

print (numpy.reshape(arr,(3,3)))

