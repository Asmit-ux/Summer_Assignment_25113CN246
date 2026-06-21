rows = int(input("Enter number of rows : "))
cols = int(input("Enter number of columns : "))

# A matrix is just a list of rows, where each row is a list of numbers
a = []
print("Enter elements of first matrix  :")
for i in range(rows):
    row = []
    for j in range(cols):
        x = int(input())
        row.append(x)
    a.append(row)

b = []
print("Enter elements of second matrix : ")
for i in range(rows):
    row = []
    for j in range(cols):
        x = int(input())
        row.append(x)
    b.append(row)

# Add matrices by adding the number at the same position in both matrices
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(a[i][j] + b[i][j])
    result.append(row)

print("Sum of matrices:")
for i in range(rows):
    for j in range(cols):
        print(result[i][j], end=" ")
    print()