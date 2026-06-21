n = int(input("Enter the  array : "))
a = []

# Binary search only works if array is sorted
print("Enter", n, "elements in sorted order:")
for i in range(n):
    x = int(input())
    a.append(x)

key = int(input("Enter element to search : "))

low = 0
high = n - 1
found = -1


while low <= high:
    mid = (low + high) // 2
    if a[mid] == key:
        found = mid
        break
    elif a[mid] < key:
        # Key must be in the right half
        low = mid + 1
    else:
        # Key must be in the left half
        high = mid - 1

if found != -1:
    print("Element found at index", found)
else:
    print("Element not found")