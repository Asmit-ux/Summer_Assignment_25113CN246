# Q.) Write a program to recursive reverse number 

def reverse(a):
    if len(a) == 1:
        return a
    return a[-1] + reverse(a[: -1])

n = input("Enter the nummber: ")
print("Reverse of",n,"is",reverse(n))
