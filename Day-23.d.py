string = input("Enter a string : ")

max_count = 0
max_char = ""

for i in string:
    count = 0

    for j in string:
        if i == j:
            count = count + 1

    if count > max_count:
        max_count = count
        max_char = i

print("Maximum occurring character is : ", max_char)
print("Frequency is : ", max_count)