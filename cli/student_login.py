
from cli.utils import colour, RED, GREEN, YELLOW, CYAN
from cli.utils import validate_password, validate_email, go_back

def login_student(students):
    print(
        colour("\n\tStudent Login\n"
        "\tEnter your registered email and password", CYAN)
    )

    while True:
        email = input("\tEmail (x to cancel): ").strip().lower()
        if email == "x":
            return go_back()

        password = input("\tPassword (x to cancel): ").strip()
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
            colour(f"\tLogin successful! Welcome, {student.name} (ID: {student.student_id})!", YELLOW)
        )
        return student

def find_student_by_credentials(students, email, password):
    for student in students:
        if student.email == email and student.password == password:
            return student

    return None