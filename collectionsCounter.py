#Hackerrank collections.Counter()

#Author: Luciano Andrade

#A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

#Task

#Raghu is a shoe shop owner. His shop has X number of shoes.
#He has a list containing the size of each shoe he has in his shop.
#There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

#Your task is to compute how much money Raghu earned.

#Input Format

#The first line contains X, the number of shoes.
#The second line contains the space separated list of all the shoe sizes in the shop.
#The third line contains N, the number of customers.
#The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.

#Print the amount of money earned by Raghu.

if __name__ == '__main__':

    X = int(input())
    shoes = list()
    shoes = input().split()
    
    n = int(input())
    
    x = list()
    for i in range(n):
        x.append(input().split())
        
    profit = 0
    for i in range(n):
        if x[i][0] in shoes:
            shoes.remove(x[i][0])
            profit = profit + int(x[i][1])
            
print(profit)
    
