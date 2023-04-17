#HackerRank Mutations challenge
#Author: Luciano Andrade

#We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

#Let's try to understand this with an example.

#You are given an immutable string, and you want to make changes to it.


def mutate_string(string, position, character):

    return string[0:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
	
	
