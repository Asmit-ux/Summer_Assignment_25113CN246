employee_names = []
employee_salary = []

while True:

    print("\n----- Salary Management System -----")
    print("1. Add Employee Salary")
    print("2. Display Salary")
    print("3. Update Salary")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        name = input("Enter Employee Name: ")
        salary = int(input("Enter Salary: "))

        employee_names.append(name)
        employee_salary.append(salary)

        print("Salary Record Added.")

    elif choice == 2:

        print("\nEmployee Salary Details")

        for i in range(len(employee_names)):
            print(employee_names[i], ":", employee_salary[i])

    elif choice == 3:

        name = input("Enter Employee Name: ")

        if name in employee_names:

            index = employee_names.index(name)

            new_salary = int(input("Enter New Salary: "))

            employee_salary[index] = new_salary

            print("Salary Updated Successfully.")

        else:
            print("Employee Not Found.")

    elif choice == 4:

        print("Thank You.")
        break

    else:
        print("Invalid Choice")