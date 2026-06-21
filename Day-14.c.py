# Q.) Write a program to second largest element

n = int(input("Enter the array : "))
a = []

print("Enter", n, "elements :")
for i in range(n):
    x = int(input())
    a.append(x)

first = a[0]
second = -999999

for i in range(1, n):
    if a[i] > first:
        second = first
        first = a[i]
    elif a[i] > second and a[i] != first:
        second = a[i]

print("Largest element =", first)
print("Second largest element =", second)