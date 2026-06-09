# Q.) Write a program to convert decimal to binary

n = int(input("Enter the decimal number: "))              # taking user input
 
binary = "" 
while n > 0:                                              # using while loop 
    binary = str(n % 2) + binary
    n = n // 2

print("The binary of n is:", binary)    