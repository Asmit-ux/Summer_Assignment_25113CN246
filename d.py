# Q.) Write a program to print armstrong numbers in a range.

a = int(input("netr the starting numer - "))
b = int(input("enter the ending number - "))

print("Armstrong numbers between", a, "and", b, "are:")

for num in range(a, b + 1):   # using for loop to iterate through the range of numbers
    order = len(str(num))     # calculating the number of digits in the number
    sum = 0                   # variable to store the sum of the powers of the digits
    temp = num                # making a copy of the original number to perform calculations

    while temp > 0:           # using while loop 
        digit = temp % 10     # extracting the last digit of the number
        sum += digit ** order  # calculating the sum of the powers of the digits
        temp //= 10           # removing the last digit from the number

    if num == sum:            # checking if the original number is equal to the calculated sum
        print(num)            # if it is, then it is an armstrong number and we print it