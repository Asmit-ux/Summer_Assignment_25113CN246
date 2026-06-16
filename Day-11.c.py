# Q.) Write a program to write a function to check prime

def prime(a):
    if a <= 1:
        return False

    for i in range(2, a):
        if a % i == 0:
            return False

    return True

num = int(input("Enter the number: "))

if prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
