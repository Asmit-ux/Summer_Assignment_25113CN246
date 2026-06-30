string = input("Enter a string : ")

result = " "

for i in string:
    if i >= 'a' and i <= 'z':
        result = result + chr(ord(i) - 32)
    else:
        result = result + i

print("Uppercase string is : ", result)