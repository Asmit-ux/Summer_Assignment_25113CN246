array = []

while True:

    print("\n----- Array Operations -----")
    print("1. Add Element")
    print("2. Display Array")
    print("3. Search Element")
    print("4. Delete Element")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        num = int(input("Enter Number: "))
        array.append(num)

    elif choice == 2:

        print("Array =", array)

    elif choice == 3:

        num = int(input("Enter Number to Search: "))

        if num in array:
            print("Element Found.")
        else:
            print("Element Not Found.")

    elif choice == 4:

        num = int(input("Enter Number to Delete: "))

        if num in array:
            array.remove(num)
            print("Element Deleted.")
        else:
            print("Element Not Found.")

    elif choice == 5:

        print("Program Ended.")
        break

    else:

        print("Invalid Choice")