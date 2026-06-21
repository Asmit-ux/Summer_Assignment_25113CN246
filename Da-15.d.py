n = int(input("Enter the array : "))
a = []

print("Enter", n, "elements :")
for i in range(n):
    x = int(input())
    a.append(x)

result = []
zero_count = 0

for i in range(n):
    if a[i] != 0:
        result.append(a[i])
    else:
        zero_count = zero_count + 1

for i in range(zero_count):
    result.append(0)

print("Array after moving zeroes to end :")
for i in range(n):
    print(result[i], end=" ")