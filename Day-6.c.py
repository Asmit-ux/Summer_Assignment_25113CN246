# Q.) Write a program to set bit in a number 

n = int(input("Enter a number - "))
pos = int(input("Enter bit position - "))

result = n | (1 << pos)

print("output will be =", result)
