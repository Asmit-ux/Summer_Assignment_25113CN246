n1 = int(input("Enter first array : "))
a = []

print("Enter", n1, "elements:")
for i in range(n1):
    x = int(input())
    a.append(x)

n2 = int(input("Enter second array : "))
b = []

print("Enter", n2, "elements :")
for i in range(n2):
    x = int(input())
    b.append(x)

# Merging just means putting all elements of both arrays together
merged = []

for i in range(n1):
    merged.append(a[i])

for i in range(n2):
    merged.append(b[i])

print("Merged array :")
for i in range(len(merged)):
    print(merged[i], end=" ")