r1 = int(input("Enter rows of first matrix : "))
c1 = int(input("Enter columns of first matrix : "))

a = []
print("Enter elements of first matrix : ")
for i in range(r1):
    row = []
    for j in range(c1):
        x = int(input())
        row.append(x)
    a.append(row)

r2 = int(input("Enter rows of second matrix : "))
c2 = int(input("Enter columns of second matrix : "))

b = []
print("Enter elements of second matrix : ")
for i in range(r2):
    row = []
    for j in range(c2):
        x = int(input())
        row.append(x)
    b.append(row)

# Multiplication is only possible if columns of first matrix
# equals rows of second matrix
if c1 != r2:
    print("Matrix multiplication not possible")
else:
    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
            # To get one value in result, multiply matching elements
            # from a row of first matrix and a column of second matrix
            # and add them all up
            sum = 0
            for k in range(c1):
                sum = sum + a[i][k] * b[k][j]
            row.append(sum)
        result.append(row)

    print("Product of matrices:")
    for i in range(r1):
        for j in range(c2):
            print(result[i][j], end=" ")
        print()