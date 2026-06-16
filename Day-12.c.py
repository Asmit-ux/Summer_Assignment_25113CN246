# Q.) Write a program to write function for fibonacci

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

n = int(input("Enter the numebr : "))
print("Fibonacci series")
fibonacci(n)

