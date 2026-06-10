# Q.) W riet a program to find repeatd character pattern 

n = int(input("Enter the number: "))

ch = ord("A")

for i in range(1, n+1):
    for j in range(i):
        print(chr(ch), end=" ")
    print()
    ch = ch + 1    