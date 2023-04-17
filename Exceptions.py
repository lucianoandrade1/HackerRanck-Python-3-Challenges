
#Hackerrank Exceptions

#Author: Luciano Andrade

#Errors detected during execution are called exceptions.

#Examples:

#ZeroDivisionError
#This error is raised when the second argument of a division or modulo operation is zero.

#ValueError
#This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.

#Task

#You are given two values a and b.
#Perform integer division and print a/b.

#Input Format

#The first line contains T, the number of test cases.
#The next  lines each contain the space separated values of a and b.

#Constraints

#0 < T < 10

#Output Format

#Print the value of a/b.
#In the case of ZeroDivisionError or ValueError, print the error code.

T = int(input())

for i in range(T):
    
    x = input().split()
    
    try:
        a = int(x[0])
        b = int(x[1])
        print(a//b)
    except ValueError as error:
        print ("Error Code:", error)
    except ZeroDivisionError as error:
        print("Error Code:",error)
		
		
		
