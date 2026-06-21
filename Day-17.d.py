n1 = int(input("Enter first array : "))
a = []

print("Enter", n1, "elements : ")
for i in range(n1):
    x = int(input())
    a.append(x)

n2 = int(input("Enter second array : "))
b = []

print("Enter", n2, "elements : ")
for i in range(n2):
    x = int(input())
    b.append(x)

print("Common elements : ")
# Compare every element of first array with every element of second array
for i in range(n1):
    for j in range(n2):
        if a[i] == b[j]:
            print(a[i], end=" ")