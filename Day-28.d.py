total_seats = 5

while True:

    print("\n----- Ticket Booking -----")
    print("Available Seats =", total_seats)

    print("1. Book Ticket")
    print("2. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        seats = int(input("How many seats do you want? "))

        if seats <= total_seats:

            total_seats = total_seats - seats

            print("Ticket Booked Successfully.")

        else:

            print("Seats Not Available.")

    elif choice == 2:

        print("Thank You")
        break

    else:

        print("Invalid Choice")