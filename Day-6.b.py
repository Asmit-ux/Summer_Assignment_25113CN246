# Q.) Write a program to cnvert binary to decimal

binary = input("Enter a binary number - ")

decimal = 0

for digit in binary:
    decimal = decimal * 2 + int(digit)

print("Decimal number =", decimal)