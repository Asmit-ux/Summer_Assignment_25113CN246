# Q.) Write a program to print half pyramid pattern

n = int(input("Enter the number: "))       # taking user input 

for i in range(1, n+1):                    # print column
    for k in range(i):                     # print row
        print("A",end =" ")
    print()

