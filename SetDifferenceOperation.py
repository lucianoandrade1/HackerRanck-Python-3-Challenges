#Hackerrank Set .difference() Operation

#Author: Luciano Andrade

#Task
#The students of District College have subscriptions to English and French newspapers. 
#Some students have subscribed only to English, some have subscribed to only French 
#and some have subscribed to both newspapers.

#You are given two sets of student roll numbers. One set has subscribed to the English 
#newspaper, and the other set is subscribed to the French newspaper. The same student 
#could be in both sets. Your task is to find the total number of students who have 
#subscribed to at least one newspaper.

#Input Format

#The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
#The second line contains n space separated roll numbers of those students.
#The third line contains b, the number of students who have subscribed to the French newspaper.
#The fourth line contains b space separated roll numbers of those students.

#Constraints

#0 < Total number of students in college < 1000

#Output Format

#Output the total number of students who are subscribed to the English newspaper only.

n = input()

eng = map(int, input().split())

b = input()

fre = map(int, input().split())

print(len(set(eng).difference(fre)))
