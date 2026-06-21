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

# Intersection means only the elements that are present in BOTH arrays
intersection = []

for i in range(n1):
    # Check if a[i] is present in array b, and not already added
    if a[i] in b and a[i] not in intersection:
        intersection.append(a[i])

print("Intersection of arrays : ")
for i in range(len(intersection)):
    print(intersection[i], end=" ")