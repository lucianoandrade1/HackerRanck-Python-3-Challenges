#HackerRank sWAP cASE challenge
#Author: Luciano Andrade

#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

#For Example:

#Www.HackerRank.com → wWW.hACKERrANK.COM
#Pythonist 2 → pYTHONIST 2

#Input Format

#A single line containing a string S.

#Constraints

#0<=len(S)<=1000

#Output Format

#Print the modified string S.

def swap_case(s):

    newS ='' 
    for a in s: 
        if a.isupper():
            newS+=(a.lower()) 
        elif a.islower(): 
            newS+=(a.upper())
        else:
            newS+= a

    return newS

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
	
	
	
