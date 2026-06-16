# Q.) Write a program to write function of armstrong

def arm(n):
    a = n
    sum = 0

    order = len(str(n))

    while a > 0:
        digit = a % 10
        sum = sum + digit ** order
        a = a // 10

n = int(input("Enter the number : "))


if n == sum:
    print(n, "is an armstrong number")

else:
    print(n, "is not an armstrong number")

