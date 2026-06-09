# Q.) Write a program to check if a number is a perfect number
a = int(input("Enter a number: "))               # Take input from the user and convert it to an integer

sum = 0                                          # Initialize a variable to store the sum of the factors of the number  
i = 1                                            # Initialize a variable to iterate through the numbers from 1 to a-1

while i < a:                                     # using while loop
    if a % i == 0:                               # Check if the number is a factor of a
        sum = sum + i                            # If it is a factor, add it to the sum
    i = i + 1                                    # increase the by 1 to check the next number

if sum == a:
    print("Number is perfect")
else:
    print("Number is not perfect")