# Q.) Write a print repeated number pattern

n = int(input("Enetr the number: "))

for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()