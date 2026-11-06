from cli.utils import validate_password, validate_email, go_back

def login_student(students):
    print(
        "\nWelcome to the Student Login.\n"
        "Please enter your registered email and password to login."
    )

    while True:
        email = input("Enter your registered email (x to cancel): ").strip().lower()
        if email == "x":
            return go_back()

        password = input("Enter your password (x to cancel): ").strip()
        if password.lower() == "x":
            return go_back()

        if not validate_email(email) or not validate_password(password):
            print("Incorrect email or password format. Please try again.")
            continue        

        student = find_student_by_credentials(students, email, password)

        if student is None:
            print(
                "Login failed. Please check your email and password. \n"
                "Please try again"
            )
            continue
        
        print(
            f"Login successful! Welcome {student.name} "
            f"(ID: {student.student_id})!"
        )
        return student

def find_student_by_credentials(students, email, password):
    for student in students:
        if student.email == email and student.password == password:
            return student

    return None