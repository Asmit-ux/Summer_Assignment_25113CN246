a = int(input("Enter a number: "))
product = 1
while a > 0:
    digits = a % 10
    product = (product * digits)
    a //= 10

print("Product of digits: ", product)