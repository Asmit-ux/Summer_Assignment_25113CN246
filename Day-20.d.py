rows = int(input("Enter number of rows : "))
cols = int(input("Enter number of columns : "))

a = []
print("Enter elements of matrix : ")
for i in range(rows):
    row = []
    for j in range(cols):
        x = int(input())
        row.append(x)
    a.append(row)

# For each column, add up all the numbers in that column
for j in range(cols):
    sum = 0
    for i in range(rows):
        sum = sum + a[i][j]
    print("Sum of column", j + 1, "=", sum)