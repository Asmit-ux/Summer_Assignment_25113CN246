# The array should contain numbers from 1 to n, but one number is missing
n = int(input("Enter n : "))
a = []

# Taking n-1 numbers because one number is missing
print("Enter", n - 1, "elements :")
for i in range(n - 1):
    x = int(input())
    a.append(x)

# Formula to find sum of numbers from 1 to n
total = n * (n + 1) // 2

# Now find the actual sum of numbers we entered
sum = 0
for i in range(n - 1):
    sum = sum + a[i]

# The difference between expected sum and actual sum is the missing number
missing = total - sum
print("Missing number is", missing)