#Hackerrank Alphabet Rangoli

#Author: Luciano Andrade

#You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

#The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).

#Function Description

#Complete the rangoli function in the editor below.

#rangoli has the following parameters:

#int size: the size of the rangoli

#Returns

#string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)

#Input Format

#Only one line of input containing size, the size of the rangoli.

#Constraints

#0 < size < 27

import string

def print_rangoli(size):

    alpha = string.ascii_lowercase

    for i in range(size-1,-size,-1):
        aux = '-'.join(alpha[size-1:abs(i):-1]+alpha[abs(i):size])
        print(aux.center(4*size-3,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
