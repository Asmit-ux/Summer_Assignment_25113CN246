# Q.) Write a program to find the nth term of the Fibonacci series.

n = int(input("Enter a number - "))   # TAKING USER INPUT

a = 0  # first term
b = 1  # second term

if n == 0:   # USING IF ELSE CONDITION
    print(a)

elif n == 1:
    print(b)    
 
else:
    for i in range(2,n+1):   # using for loop
        c = a + b            # calculating the next term 
        a = b                # updating the value of a and 
        b = c                # b for the next iteration
    print(b) 

