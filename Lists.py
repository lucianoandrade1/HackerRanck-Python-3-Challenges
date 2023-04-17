#HackerRank Lists challenge
#Author: Luciano Andrade

#Consider a list (list = []). You can perform the following commands:

#insert i e: Insert integer e at position i.
#print: Print the list.
#remove e: Delete the first occurrence of integer e.
#append e: Insert integer e at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.

#Initialize your list and read in the value of n followed by n lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    N = int(input())

    myList = []
    for n in range(N):
        inp = input().split(" ")

        if inp[0]=="insert":
            myList.insert(int(inp[1]), int(inp[2]))
        if inp[0]=="remove":
            myList.remove(int(inp[1]))
        if inp[0]=="append":
            myList.append(int(inp[1]))
        if inp[0]=="pop":
            myList.pop(-1)
        if inp[0]=="sort":
            myList.sort()
        if inp[0]=="reverse":
            myList.reverse()
        if inp[0]=="print":
            print(myList)

