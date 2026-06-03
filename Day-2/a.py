a = int(input('Enter a number: '))
s = 0
while a:
    s += a % 10
    a //= 10
print(s)    
