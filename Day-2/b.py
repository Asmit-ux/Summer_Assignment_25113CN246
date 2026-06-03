a = int(input("Enter a number: "))
reverse  = 0 
while a > 0:
    digits = a % 10
    reverse = (reverse * 10) + digits
    a //= 10
print("Reversed number: ", reverse)


