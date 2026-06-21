n = int(input("Enter the array : "))
a = []

print("Enter", n, "elements :")
for i in range(n):
    x = int(input())
    a.append(x)

# We will only add a number to result if it is not already there
result = []

for i in range(n):
    if a[i] not in result:
        result.append(a[i])

print("Array after removing duplicates :")
for i in range(len(result)):
    print(result[i], end=" ")