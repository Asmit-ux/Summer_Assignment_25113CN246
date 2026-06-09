# Q.) Writea program to check if a number is a strong number

def fact(a):                                            # using recursion to find the factorial of a number
    if a == 0 or a == 1: 
        return 1
    else:
        return a * fact(a - 1)

a = int(input("Enter a number - "))                         

temp = a                    # making a copy of the original number to perform calculations
sum = 0                     # variable to store the sum of the factorials of the digits
 
while temp > 0:                                # using while loop
    digit = temp % 10                          # exrtacting the last digit of the number
    sum = sum +fact(digit)                     # calculating the sum of the factorials of the digits
    temp = temp // 10                          # removing the last digit from the number

if a == sum:
    print(a, "is a strong number")

else:
    print(a, "is not a strong number")