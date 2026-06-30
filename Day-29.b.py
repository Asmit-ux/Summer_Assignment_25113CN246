while True:

    print("\n----- Calculator -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 5:
        print("Calculator Closed.")
        break

    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    if choice == 1:
        print("Answer =", num1 + num2)

    elif choice == 2:
        print("Answer =", num1 - num2)

    elif choice == 3:
        print("Answer =", num1 * num2)

    elif choice == 4:

        if num2 != 0:
            print("Answer =", num1 / num2)
        else:
            print("Division by zero is not possible.")

    else:
        print("Invalid Choice")