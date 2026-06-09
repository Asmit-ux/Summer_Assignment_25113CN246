# Q.) Write a program to find X^n without pow()

x = int(input("Enter X: "))       # taking input from x
n = int(input("Enter n: "))       # taking input from user for n

result = 1                        # initializing result to 1

for i in range(n):                # using for loop
    result = result * x             

print("Answer =", result)