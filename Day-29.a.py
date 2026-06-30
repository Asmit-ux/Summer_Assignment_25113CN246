contact_names = []
contact_numbers = []

while True:

    print("\n----- Contact Management System -----")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        name = input("Enter Name: ")
        number = input("Enter Mobile Number: ")

        contact_names.append(name)
        contact_numbers.append(number)

        print("Contact Added Successfully.")

    elif choice == 2:

        print("\nContact List")

        for i in range(len(contact_names)):
            print(contact_names[i], "-", contact_numbers[i])

    elif choice == 3:

        name = input("Enter Name to Search: ")

        if name in contact_names:
            index = contact_names.index(name)
            print("Mobile Number:", contact_numbers[index])
        else:
            print("Contact Not Found.")

    elif choice == 4:

        print("Thank You")
        break

    else:

        print("Invalid Choice")