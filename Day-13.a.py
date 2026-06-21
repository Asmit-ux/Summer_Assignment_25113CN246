# Q.) Write a program to input and display array

n = int(input("Enter the array: "))
a = []

print("Enter", n, "elements:")
for i in range(n):
    x = int(input())
    a.append(x)

print("The array elements are:")
for i in range(n):
    print(a[i], end=" ")

