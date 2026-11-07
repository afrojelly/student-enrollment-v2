from cli.utils import colour, RED, GREEN, YELLOW, CYAN
import random #student ID generation

from cli.student import Student
from cli.utils import validate_email, validate_password, go_back

def register_student(students, database):
    print(colour("\nStudent Registration.", CYAN))

    # name input and validation
    while True:
        name = input("\tName (x to cancel): ").strip()

        if not name:
            print(colour("\tName cannot be empty, try again.", RED))
            continue

        if name.lower() == "x":
            return go_back(students)

        break

    # email input and validation
    while True:
        email = input("\tEmail (firstname.lastname@university.com, or x to cancel): ").strip().lower()

        if not email:
            print(colour("\tEmail cannot be empty, try again.", RED))
            continue

        if email == "x":
            return go_back(students)

        if not validate_email(email):
            print(colour("\tInvalid email. Use the format: firstname.lastname@university.com", RED))
            continue

        existing_emails = {student.email for student in students}
        if email in existing_emails:
            print(colour("\tThis email is already registered. Please try another email.", RED))
            continue

        break

    # password input and validation
    while True:
        password = input("\tPassword (comfirm format, or x to cancel): ").strip()

        if not password:
            print(colour("\tPassword cannot be empty, try again.", RED))
            continue

        if password.lower() == "x":
            return go_back(students)
        
        if not validate_password(password):
            print(colour(
                "\tInvalid password. "
                "\n\tIt must start with an uppercase letter, "  
                "\n\tcontain more than 5 letters, followed by at least 3 digits. "  
                "\n\tPlease try again.", RED)
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
        colour("\tRegistration successful!\n"
        "\tPlease login with your email and password.", GREEN)
    )
    print(colour(f"\tYour student ID is: {student.student_id}", YELLOW))

    return students # return the updated list

# Auto-student ID generation
def generate_student_id(students):
    existing_ids = {student.student_id for student in students}

    if len(existing_ids) >= 999_999:
        print(colour(
            "\tAll available student IDs have been used. "
            "\tA new student ID cannot be generated.\n"
            "\tPlease contact the administrator for assistance."
        , RED))
        return None

    while True:
        student_id = str(random.randint(1, 999_999)).zfill(6)
        if student_id not in existing_ids:
            return student_id