name = input("Enter Student Name: ")

sub1 = int(input("Enter Marks of Subject 1 : "))
sub2 = int(input("Enter Marks of Subject 2 : "))
sub3 = int(input("Enter Marks of Subject 3 : "))
sub4 = int(input("Enter Marks of Subject 4 : "))
sub5 = int(input("Enter Marks of Subject 5 : "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

print("\n------ Marksheet ------")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A+")

elif percentage >= 75:
    print("Grade: A")

elif percentage >= 60:
    print("Grade: B")

elif percentage >= 40:
    print("Grade: C")

else:
    print("Grade: Fail")