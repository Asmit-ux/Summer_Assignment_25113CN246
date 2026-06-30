employee_names = []
employee_salary = []

while True:

    print("\n----- Employee Management System -----")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Employee Name: ")
        salary = int(input("Enter Salary: "))

        employee_names.append(name)
        employee_salary.append(salary)

        print("Employee Added Successfully.")

    elif choice == 2:

        print("\nEmployee Details")

        for i in range(len(employee_names)):
            print("Name:", employee_names[i], "Salary:", employee_salary[i])

    elif choice == 3:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")