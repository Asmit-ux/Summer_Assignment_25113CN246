n = int(input("Enter size of square matrix (n x n) : "))

a = []
print("Enter elements of matrix : ")
for i in range(n):
    row = []
    for j in range(n):
        x = int(input())
        row.append(x)
    a.append(row)

# Diagonal elements are the ones where row number equals column number
# Example: a[0][0], a[1][1], a[2][2] and so on
sum = 0
for i in range(n):
    sum = sum + a[i][i]

print("Diagonal sum =", sum)