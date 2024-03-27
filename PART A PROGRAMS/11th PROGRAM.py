def accept_details():
    students = []
    while True:
        student = {}
        student['name'] = input("Enter student name (press q to exit): ")
        if student['name'].lower() == 'q':
            break
        student['roll_number'] = input("Enter roll number: ")
        student['marks'] = float(input("Enter marks: "))
        students.append(student)
    return students

def write_details(students):
    with open('student_details.txt', 'w') as file:
        for student in students:
            file.write(student['name'] + ',')
            file.write(student['roll_number'] + ',')
            file.write(str(student['marks']) + '\n')

def display_details():
    with open('student_details.txt', 'r') as file:
        print("Name\tRoll Number\tMarks")
        for line in file:
            name, roll_number, marks = line.strip().split(',')
            print(f"{name}\t{roll_number}\t\t{marks}")

students = accept_details()
write_details(students)
display_details()
input(" ")
