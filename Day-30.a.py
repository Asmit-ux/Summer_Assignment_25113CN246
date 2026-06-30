student_names = []
student_class = []

while True:

    print("\n----- Student Record System -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:

        name = input("Enter Student Name : ")
        clas = input("Enter Class : ")

        student_names.append(name)
        student_class.append(clas)

        print("Student Added Successfully.")

    elif choice == 2:

        print("\nStudent Records")

        for i in range(len(student_names)):
            print("Name:", student_names[i], "Class:", student_class[i])

    elif choice == 3:

        name = input("Enter Student Name: ")

        if name in student_names:

            index = student_names.index(name)

            print("Name:", student_names[index])
            print("Class:", student_class[index])

        else:

            print("Student Not Found.")

    elif choice == 4:

        print("Thank You")
        break

    else:

        print("Invalid Choice")