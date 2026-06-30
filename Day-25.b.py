string1 = input("Enter first string : ")
string2 = input("Enter second string : ")

print("Common characters are : ")

for i in string1:
    if i in string2:
        print(i)