books = []

while True:

    print("\n----- Library Management -----")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        book = input("Enter Book Name: ")
        books.append(book)
        print("Book Added Successfully.")

    elif choice == 2:

        print("\nAvailable Books")

        for i in books:
            print(i)

    elif choice == 3:

        print("Thank You")
        break

    else:
        print("Invalid Choice")