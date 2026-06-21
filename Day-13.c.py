# Q.) Write a program to find smallest and largest element

n = int(input("Enter the array : "))
a = []

print("Enter", n, "elements:")
for i in range(n):
    x = int(input())
    a.append(x)

max = a[0]
min = a[0]

for i in range(1, n):
    if a[i] > max:
        max = a[i]
    if a[i] < min:
        min = a[i]

print("Largest element =", max)
print("Smallest element =", min)