#Hackerrank Finding the percentage challenge
#Author: Luciano Andrade

#You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer N followed by the names and marks for N students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

#Input Format

#The first line contains the integer N, the number of students. The next N lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

#Constraints

#2<=N<=10
#0<=Marks<=100

#Output Format

#Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

def Avg(lst): 
    return sum(lst) / len(lst) 

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print('{:.2f}'.format(Avg(student_marks[query_name])))
