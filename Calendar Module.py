#Hackerrank Calendar Module

#Author: Luciano Andrade

#Task

#You are given a date. Your task is to find what the day is on that date.

#Input Format

#A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

#Constraints

#2000 < year < 3000

#Output Format

#Output the correct day in capital letters.

#Sample Input

#08 05 2015

#Sample Output

#WEDNESDAY

#Explanation

#The day on August 5th 2015 was WEDNESDAY.

import calendar

def day_of_week(year, month, day):

    switcher = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }
    
    return switcher.get(calendar.weekday(int(year), int(month), int(day))).upper()

month, day, year = input().split()

print (day_of_week(year, month, day))



