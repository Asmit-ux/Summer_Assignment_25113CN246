# Q.) Wriet a program to check armstrong number

n = int(input("Enter a number - "))

a = n    # making a copy of the original number to perform calculations
sum = 0  # variable to store the sum of the cubes of the digits

order = len(str(n))   # calculating the number of digits in the number

while a > 0:                                    # using while loop 
    digit = a % 10                              # exrtacting the last digit of the number  
    sum = sum + digit ** order                  # calculating the sum of the powers of the digits     
    a = a // 10                                 # removing the last digit from the number

if n == sum:
    print(n, "is an armstrong number")

else:
    print(n, "is not an armstrong number")

