## Jacob Elsbury
## Student GPA Database
## This program is a simple data entry app that allows you to enter in students names and GPAs. The app when they tell you if the student should receive any special recognition.



student_names = []
student_gpas = []

while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ").strip()

    if last_name == 'ZZZ':
        break

    first_name = input("Enter the student's first name: ").strip()

    while True:
        try:
            gpa = float(input("Enter the student's GPA: "))
            break
        except ValueError:
            print("Invalid GPA. Please enter a numeric value.")
    
    student_names.append((first_name, last_name))
    student_gpas.append(gpa)

print("\nStudent Records:")
for i in range(len(student_names)):
    first_name, last_name = student_names[i]
    gpa = student_gpas[i]

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made Honor Roll. ")
    else:
        print(f"{first_name} {last_name} did not qualify for any special recognition.")