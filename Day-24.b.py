string = input("Enter a string : ")

count = 1
result = " "

for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
        count = count + 1
    else:
        result = result + string[i] + str(count)
        count = 1

result = result + string[-1] + str(count)

print("Compressed String:", result)    