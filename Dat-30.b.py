books = []

while True:

    print("\n----- Mini Library -----")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Display Books")
    print("4. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:

        book = input("Enter Book Name : ")

        books.append(book)

        print("Book Added Successfully.")

    elif choice == 2:

        book = input("Enter Book Name to Issue : ")

        if book in books:

            books.remove(book)

            print("Book Issued Successfully.")

        else:

            print("Book Not Available.")

    elif choice == 3:

        print("\nAvailable Books")

        for i in books:
            print(i)

    elif choice == 4:

        print("Thank You")
        break

    else:

        print("Invalid Choice")