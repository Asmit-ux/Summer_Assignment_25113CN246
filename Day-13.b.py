# Q.) Wriet a program to find sum and average of an array

n = int(input("Enter the array : "))
a = []

print("Enter", n, "elements:")
for i in range(n):
    x = int(input())
    a.append(x)

sum = 0
for i in range(n):
    sum = sum + a[i]

avg = sum / n

print("Sum =", sum)
print("Average =", avg)