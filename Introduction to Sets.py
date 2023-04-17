#Hackerrank Introduction to Sets

#Author: Luciano Andrade

#A set is an unordered collection of elements without duplicate entries.

#When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

#Basically, sets are used for membership testing and eliminating duplicate entries.

#Task

#Now, let's use our knowledge of sets and help Mickey.

#Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student 
#Mickey to compute the average of all the plants with distinct heights in her greenhouse.

#Function Description

#Complete the average function in the editor below.

#average has the following parameters:

#int arr: an array of integers
#Returns

#float: the resulting float value rounded to 3 places after the decimal
#Input Format

#The first line contains the integer, N, the size of arr.
#The second line contains the N space-separated integers, arr[i].

#Constraints

#0<=N<=100

from functools import reduce

def average(array):
    
    return round(reduce(lambda a, b: a + b, set(array)) / len(set(array)),3)
        

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
	
	
	
