# Q.) Wriet a program to print factor of a number 

a = int(input("Enter a number: "))               # Take input from the user and convert it to an integer

i = 1                                           
while i <= a:                                    # using while loop
    if a % i == 0:                               # Check if the number is a factor of a
        print(i)                                 # If it is a factor, print it
    i = i + 1                                    # increase the by 1 to check the next number

print("Factors of", a, "are: ")                  # Print the factors of the number
