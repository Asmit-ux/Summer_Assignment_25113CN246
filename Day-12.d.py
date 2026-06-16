# Q.) Write a program to write function for perfect number

def perfect(n):
    sum = 0
    i = 1

    while i < n:
        if n % i == 0:
            sum = sum + i
        i = i + 1

n = int(input("Enter the number : "))

if sum == n:
    print("Number is perfect")
else:
    print("Number is not perfect")