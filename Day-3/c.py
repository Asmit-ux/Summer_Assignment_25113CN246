a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

while b != 0:
    temp = b
    b = a % b
    a = temp

print("GCD is", a)

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

while b != 0:
    a , b = b , a % b

print("GCD is", a)