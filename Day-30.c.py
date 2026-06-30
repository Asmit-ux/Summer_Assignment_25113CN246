employee_names = []
employee_department = []

while True:

    print("\n----- Employee Management -----")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:

        name = input("Enter Employee Name : ")
        department = input("Enter Department : ")

        employee_names.append(name)
        employee_department.append(department)

        print("Employee Added Successfully.")

    elif choice == 2:

        print("\nEmployee Details")

        for i in range(len(employee_names)):
            print(employee_names[i], "-", employee_department[i])

    elif choice == 3:

        name = input("Enter Employee Name: ")

        if name in employee_names:

            index = employee_names.index(name)

            print("Department:", employee_department[index])

        else:

            print("Employee Not Found.")

    elif choice == 4:

        print("Thank You")
        break

    else:

        print("Invalid Choice")