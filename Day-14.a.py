# Q.) Write a program to linear search

n = int(input("Enter the array : "))
a = []

print("Enter", n, "elements :")
for i in range(n):
    x = int(input())
    a.append(x)

key = int(input("Enter element to search : "))
found = -1

for i in range(n):
    if a[i] == key:
        found = i
        break

if found != -1:
    print("Element found at index", found)
else:
    print("Element not found")