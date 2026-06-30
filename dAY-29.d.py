item_names = []
item_quantity = []

while True:

    print("\n----- Inventory Management -----")
    print("1. Add Item")
    print("2. Display Items")
    print("3. Update Quantity")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        name = input("Enter Item Name: ")
        quantity = int(input("Enter Quantity: "))

        item_names.append(name)
        item_quantity.append(quantity)

        print("Item Added Successfully.")

    elif choice == 2:

        print("\nInventory List")

        for i in range(len(item_names)):
            print(item_names[i], "-", item_quantity[i])

    elif choice == 3:

        name = input("Enter Item Name: ")

        if name in item_names:

            index = item_names.index(name)

            quantity = int(input("Enter New Quantity: "))

            item_quantity[index] = quantity

            print("Quantity Updated Successfully.")

        else:

            print("Item Not Found.")

    elif choice == 4:

        print("Program Closed.")
        break

    else:

        print("Invalid Choice")