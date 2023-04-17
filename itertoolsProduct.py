#Hackerrank itertools.product()
#Author: Luciano Andrade

#This tool computes the cartesian product of input iterables.

#It is equivalent to nested for-loops.

#For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

#Task

#You are given a two lists A and B. Your task is to compute their cartesian product X.

#Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

if __name__ == '__main__':
    
    a = input().split()
    b = input().split()
    
l = [(int(x),int(y)) for x in a for y in b]

for e in l:
    print(e, end =" ")
