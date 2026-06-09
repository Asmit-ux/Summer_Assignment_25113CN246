# Q.) Write a program tp recursive fibonacci.

def fib(n):
    if n <= 0:
        return n
    return fib(n - 1) + fib(n - 2)


n = int(input("Enter the number - "))         #taking input from the user
print("Fibonacci of series up to", n, "terms:") 

for i in range(n):
    print(fib(i), end=" ")