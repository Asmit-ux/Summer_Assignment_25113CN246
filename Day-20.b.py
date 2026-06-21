n = int(input("Enter size of square matrix (n x n) : "))

a = []
print("Enter elements of matrix : ")
for i in range(n):
    row = []
    for j in range(n):
        x = int(input())
        row.append(x)
    a.append(row)

# A matrix is symmetric if a[i][j] is always equal to a[j][i]
symmetric = True

for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            symmetric = False

if symmetric == True:
    print("The matrix is symmetric")
else:
    print("The matrix is not symmetric")