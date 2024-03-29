#Hackerrank Collections.deque()

#Author: Luciano Andrade

#Task

#Perform append, pop, popleft and appendleft methods on an empty deque d.

#Input Format

#The first line contains an integer N, the number of operations.
#The next N lines contains the space separated names of methods and their values.

#Constraints

#0 < N <= 100

#Output Format

#Print the space separated elements of deque d.

from collections import deque

N = int(input())

d = deque()
for _ in range(N):
    command = input().split()
    
    if command[0] == 'append':
    
        d.append(command[1])
        
    elif command[0] == 'pop':
    
        d.pop()
    
    elif command[0] == 'popleft':
    
        d.popleft()
    
    elif command[0] == 'appendleft':
    
        d.appendleft(command[1])
        
    else:
        print('Unknown command') 
    
print(' '.join(d))
    
	
	
