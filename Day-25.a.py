array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]

result = []

for i in array1:
    result.append(i)

for i in array2:
    result.append(i)

result.sort()

print("Merged Array : ")
print(result)