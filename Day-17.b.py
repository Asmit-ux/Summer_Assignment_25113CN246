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

# Union means all unique elements from both arrays combined
union = []

# Add elements from first array (only if not already added)
for i in range(n1):
    if a[i] not in union:
        union.append(a[i])

# Add elements from second array (only if not already added)
for i in range(n2):
    if b[i] not in union:
        union.append(b[i])

print("Union of arrays :")
for i in range(len(union)):
    print(union[i], end=" ")