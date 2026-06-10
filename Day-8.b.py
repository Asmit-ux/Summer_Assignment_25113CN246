# Q.) Write a program to print number triangle

n = 6

for i in range(1, n+1):                   # using for loop to print the column
    for j in range(1, i):                 # using for loop to print row
        print(j,end =" ")
    print()