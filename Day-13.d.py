# Q.) Write a program to count evena and odd element

n = int(input("Enter the array : "))
a = []

print("Enter", n, "elements:")
for i in range(n):
    x = int(input())
    a.append(x)

even = 0
odd = 0

for i in range(n):
    if a[i] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even elements =", even)
print("Odd elements =", odd)