n = int(input("Enter the array : "))
a = []

print("Enter", n, "elements :")
for i in range(n):
    x = int(input())
    a.append(x)

# We will check each number and count how many times it repeats
max_freq = 0
max_element = a[0]

for i in range(n):
    count = 0
    # Count how many times a[i] appears in the whole array
    for j in range(n):
        if a[j] == a[i]:
            count = count + 1
    # If this count is bigger than what we found before, update it
    if count > max_freq:
        max_freq = count
        max_element = a[i]

print("Element with maximum frequency =", max_element)
print("It appears", max_freq, "times")