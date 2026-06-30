string = input("Enter a string : ")

for i in string:
    count = 0

    for j in string:
        if i == j:
            count = count + 1

    if count > 1:
        print("First repeating character is : ", i)
        break