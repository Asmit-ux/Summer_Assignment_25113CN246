n = int(input("Enter the array : "))
a = []

print("Enter", n, "elements :")
for i in range(n):
    x = int(input())
    a.append(x)

target = int(input("Enter the target sum : "))
found = False

# Check every possible pair of numbers
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == target:
            print("Pair found:", a[i], "and", a[j])
            found = True

if found == False:
    print("No pair found with the given sum")