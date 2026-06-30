student_names = []
student_marks = []

while True:

    print("\n----- Student Record Management -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Student Name: ")
        marks = int(input("Enter Student Marks: "))

        student_names.append(name)
        student_marks.append(marks)

        print("Student Record Added Successfully.")

    elif choice == 2:

        print("\nStudent Records")

        for i in range(len(student_names)):
            print("Name:", student_names[i], "Marks:", student_marks[i])

    elif choice == 3:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")