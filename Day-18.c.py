n = int(input("Enter the array : "))
a = []

print("Enter", n, "elements :")
for i in range(n):
    x = int(input())
    a.append(x)


for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j
    
    temp = a[i]
    a[i] = a[min_index]
    a[min_index] = temp

print("Sorted array (ascending) :")
for i in range(n):
    print(a[i], end=" ")