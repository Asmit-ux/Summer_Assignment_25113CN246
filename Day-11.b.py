# Q.) Write a program to wriet function to find maximum

def maximum(a,b,c):
    if(a >= b and a > c):
        return a
    elif(b >= a and b >= c):
        return b
    else:
        return c
print(maximum(a = 5,b = 89,c = 23))


def maximum(a,b,c):
    if(a >= b and a >= c):
        print(a)
    elif(b >= a and b >= c):
        print(b)
    else:
        print(c)
maximum(55,39,23)