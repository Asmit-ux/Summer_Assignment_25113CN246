n = int(input("Enter the array: "))
a = []

print("Enter", n, "elements :")
for i in range(n):
    x = int(input())
    a.append(x)

d = int(input("Enter number of positions to rotate left : "))
d = d % n

result = []

for i in range(d, n):
    result.append(a[i])

for i in range(0, d):
    result.append(a[i])

print("Array after left rotation :")
for i in range(n):
    print(result[i], end=" ")