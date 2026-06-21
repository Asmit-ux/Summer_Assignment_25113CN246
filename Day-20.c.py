rows = int(input("Enter number of rows : "))
cols = int(input("Enter number of columns : "))

a = []
print("Enter elements of matrix :")
for i in range(rows):
    row = []
    for j in range(cols):
        x = int(input())
        row.append(x)
    a.append(row)

# For each row, add up all the numbers in that row
for i in range(rows):
    sum = 0
    for j in range(cols):
        sum = sum + a[i][j]
    print("Sum of row", i + 1, "=", sum)