a = int(input("Enter a number: "))

if a < 2:
    print("number is not prime")

else:
    for i in range(2,a):
        if a % i == 0:
            print("number is not prime")
            break
    else:
        print("number is prime")
