# Q.) Write a program to find largest prime factor

a = int(input("Enter a number: "))               # Take input from the user and convert it to an integer

i = 2                                            # Initialize a variable to start from 2
while i <= a:                                    # using while loop
    if a % i == 0:                               # Check if the number is a factor of a
        a = a // i                               # If it is a factor, divide a by i to reduce it
    else:
        i = i + 1                                # If it is not a factor, increase i by 1 to check the next number

print("Largest prime factor is:", i)             # Print the largest prime factor of the number

