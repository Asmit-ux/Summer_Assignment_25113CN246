# Q.) Write a program to print the Fibonacci series up to n terms.

n = int(input("Enter the number - "))

a = 0   # first term
b = 1   # second term

for i in range(n):          # using for loop
    print(a, end=" ")  
    c = a + b               # calculating the next term
    a = b                   # updating the value of a and
    b = c                   # b for the next iteration

      
# def fib(n):                
#     if n <= 0:
#         return n
#     return fib(n-1) + fib(n-2)

# n = int(input("Enter the number - "))
# print("Fibonacci series up to", n ,"terms:")

# for i in range(n):
#     print(fib(i), end="")