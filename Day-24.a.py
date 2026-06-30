string1 = input("Enter first string : ")
string2 = input("Enter second string : ")

temp = string1 + string1

if string2 in temp:
    print("String is Rotation")
else:
    print("String is Not Rotation")