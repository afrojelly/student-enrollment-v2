
from cli.utils import colour, RED, GREEN, YELLOW, CYAN
from cli.utils import validate_password, validate_email, go_back

def login_student(students):
    print(
        colour("\nWelcome to the Student Login.\n"
        "Please enter your registered email and password to login.", CYAN)
    )

    while True:
        email = input("\tEnter your registered email (x to cancel): ").strip().lower()
        if email == "x":
            return go_back()

        password = input("\tEnter your password (x to cancel): ").strip()
        if password.lower() == "x":
            return go_back()

        if not validate_email(email) or not validate_password(password):
            print(colour("\tIncorrect email or password format. Please try again.", RED))
            continue        

        student = find_student_by_credentials(students, email, password)

        if student is None:
            print(
                colour("\tLogin failed. Please check your email and password. \n"
                "\tPlease try again", RED)
            )
            continue
        
        print(
            colour(f"\tLogin successful! Welcome {student.name} "
            f"(ID: {student.student_id})!", GREEN)
        )
        return student

def find_student_by_credentials(students, email, password):
    for student in students:
        if student.email == email and student.password == password:
            return student

    return None