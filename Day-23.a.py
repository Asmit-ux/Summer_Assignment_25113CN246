string = input("Enter a string : ")

result = ""

for i in string:
    if i != " ":
        result = result + i

print("String after removing spaces : ")
print(result)
