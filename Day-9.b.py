# Q.) Write a program to print reverse number 

n = 7

for i in range(1, n-1):
    for j in range(i, n-1):
        print(j, end=" ")
    print()    