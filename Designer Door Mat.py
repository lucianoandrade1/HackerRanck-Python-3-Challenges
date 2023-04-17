#HackerRank Designer Door Mat challenge
#Author: Luciano Carli Moreira de Andrade

#Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

#Mat size must be N X M. ( is an odd natural number, and M is 3 times N.)
#The design should have 'WELCOME' written in the center.
#The design pattern should only use |, . and - characters.

N, M = map(int,input().split())

pattern = [('.|.'*(2*i + 1)).center(M, '-') for i in range(N//2)]

print('\n'.join(pattern + ['WELCOME'.center(M, '-')] + pattern[::-1]))

