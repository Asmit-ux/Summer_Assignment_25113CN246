n = int(input("Enter the array : "))
a = []

print("Enter", n, "elements :")
for i in range(n):
    x = int(input())
    a.append(x)

start = 0
end = n - 1

while start < end:
    temp = a[start]
    a[start] = a[end]
    a[end] = temp
    start = start + 1
    end = end - 1

print("Reversed array :")
for i in range(n):
    print(a[i], end=" ")