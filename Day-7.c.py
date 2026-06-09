# Q.) Wriet a program to recursive sum of digits.

def sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum(n//10)


n = int(input("Enter the numner - "))
print("Sum of the", n ,"is", sum(n))
        