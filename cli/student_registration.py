import random #student ID generation

from cli.student import Student
from cli.utils import validate_email, validate_password, go_back

def register_student(students, database):
    print("\nWelcome to the Student Registration.")

    # name input and validation
    while True:
        name = input("Enter your name (x to cancel): ").strip()

        if not name:
            print("Name cannot be empty, try again.")
            continue

        if name.lower() == "x":
            return go_back(students)

        break

    # email input and validation
    while True:
        email = input("Enter your email (firstname.lastname@university.com, or x to cancel): ").strip()

        if not email:
            print("Email cannot be empty, try again.")
            continue

        if email.lower() == "x":
            return go_back(students)

        if not validate_email(email):
            print("Invalid email. Use the format: firstname.lastname@university.com")
            continue

        existing_emails = {student.email for student in students}
        if email in existing_emails:
            print("This email is already registered. Please try another email.")
            continue

        break

    # password input and validation
    while True:
        password = input("Enter your password (Password123, or x to cancel): ").strip()

        if not password:
            print("Password cannot be empty, try again.")
            continue

        if password.lower() == "x":
            return go_back(students)

        if not validate_password(password):
            print(
                "Invalid password.\n"
                "It must start with an uppercase letter, "
                "contain at least 5 letters, and end with at least 3 digits.\n"
                "Please try again."
            )
            continue

        break

    student_id = generate_student_id(students)

    if student_id is None:
        return students

    student = Student(name, email, password, student_id)
    students.append(student)

    database.save_student(students)

    print(
        "Registration successful!\n"
        "Please login with your email and password."
    )
    print(f"Your student ID is: {student.student_id}")

    return students # return the updated list

# Auto-student ID generation
def generate_student_id(students):
    existing_ids = {student.student_id for student in students}

    if len(existing_ids) >= 999_999:
        print(
            "All available student IDs have been used. "
            "A new student ID cannot be generated.\n"
            "Please contact the administrator for assistance."
        )
        return None

    while True:
        student_id = str(random.randint(1, 999_999)).zfill(6)
        if student_id not in existing_ids:
            return student_id