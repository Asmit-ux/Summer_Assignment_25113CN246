# Q.) Write a program to find duplicate in array

n = int(input("Enter the array : "))
a = []

print("Enter", n, "elements :")
for i in range(n):
    x = int(input())
    a.append(x)

print("Duplicate elements :")
for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            print(a[i])
            break