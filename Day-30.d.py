student_names = []
student_marks = []

def add_student():

    name = input("Enter Student Name : ")
    marks = int(input("Enter Marks : "))

    student_names.append(name)
    student_marks.append(marks)

    print("Student Added Successfully.")

def display_students():

    print("\nStudent Records")

    for i in range(len(student_names)):
        print(student_names[i], "-", student_marks[i])

def search_student():

    name = input("Enter Student Name : ")

    if name in student_names:

        index = student_names.index(name)

        print("Name:", student_names[index])
        print("Marks:", student_marks[index])

    else:

        print("Student Not Found.")

while True:

    print("\n----- Student Management Project -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        print("Project Closed.")
        break

    else:
        print("Invalid Choice")