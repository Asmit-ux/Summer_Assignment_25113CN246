balance = 10000

while True:

    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance =", balance)

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Money Deposited Successfully.")

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance = balance - amount
            print("Please collect your cash.")
        else:
            print("Insufficient Balance.")

    elif choice == 4:
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid Choice.")