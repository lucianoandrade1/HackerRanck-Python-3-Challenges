#Hackerrank Capitalize!
#Author: Luciano Andrade

#Task

#You are the manager of a supermarket.
#You have a list of N items together with their prices that consumers bought on a particular day.
#Your task is to print each item_name and net_price in order of its first occurrence.

#item_name = Name of the item.
#net_price = Quantity of the item sold multiplied by the price of each item.

#Input Format

#The first line contains the number of items, .
#The next N lines contains the item's name and price, separated by a space.

#Constraints

#0 < N <= 100

#Output Format

#Print the item_name and net_price in order of its first occurrence.

N = int(input())

ordinary_dictionary = {}
for _ in range(N):
    
    item = input().split()
    
    if ' '.join(item[:-1]) in ordinary_dictionary:
        ordinary_dictionary[' '.join(item[:-1])] = ordinary_dictionary.get(' '.join(item[:-1])) + int(item[::-1][0])
        
    else:
        ordinary_dictionary[' '.join(item[:-1])] = int(item[::-1][0])
    
for key, value in ordinary_dictionary.items():
    print(key + ' ' + str(value))
	
	
