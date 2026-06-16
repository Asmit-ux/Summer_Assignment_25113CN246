# Q.) Write a program to write function for palindrome

def palindrome(n):
    original = a
    reverse = 0 

    while a > 0:
       digits = a % 10
       reverse = (reverse * 10) + digits
       a //= 10

    if (original == reverse):
        print("The number is a palindrome.")

    else:
        print("The number is not a palindrome.")