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

# Transpose means turning rows into columns
# The element at row i, column j moves to row j, column i
result = []
for i in range(cols):
    row = []
    for j in range(rows):
        row.append(a[j][i])
    result.append(row)

print("Transpose of matrix:")
for i in range(cols):
    for j in range(rows):
        print(result[i][j], end=" ")
    print()