names = []

n = int(input("How many names do you want to enter? "))

for i in range(n):
    name = input("Enter name : ")
    names.append(name)

names.sort()

print("Names in Alphabetical Order : ")

for i in names:
    print(i)