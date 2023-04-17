#HackerRank String Formatting challenge
#Author: Luciano Andrade

#Given an integer, n, print the following values for each integer i from 1 to n:

#Decimal
#Octal
#Hexadecimal (capitalized)
#Binary

#The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of n.

#Input Format

#A single integer denoting n.

#Constraints

#1<=n<=99

#Output Format

#Print n lines where each line i (in the range 1<=i<=n) contains the respective decimal, octal, capitalized hexadecimal, and binary values of i. Each printed value must be formatted to the width of the binary value of n.

def print_formatted(number):

    for i in range(1,number+1):
        l = len(str(bin(number)[2:])) + 1
        l1 = len(str(i))
                
        d = str(i).rjust(l - 1,' ')
        o = str(oct(i))[2:].rjust(l,' ')
        h = str(hex(i))[2:].upper().rjust(l,' ')
        b = str(bin(i))[2:].rjust(l,' ')

        print("".join([d,o,h,b]))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
	
	
	
	
