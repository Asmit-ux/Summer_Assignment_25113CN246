# Q.) Write a program to frequency of an element

n = int(input("Enter the array : "))
a = []

print("Enter", n, "elements :")
for i in range(n):
    x = int(input())
    a.append(x)

key = int(input("Enter element to check frequency : "))
count = 0

for i in range(n):
    if a[i] == key:
        count = count + 1

print("Frequency of", key, "=", count)