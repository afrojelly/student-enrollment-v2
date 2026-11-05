
from cli.utils import validate_password, validate_email, go_back


def validate_login(students, email, password):
    for student in students:
        if student.email == email and student.password == password:
            return student

    return None
def login_student(students):
    print("\n welcome to the Student Login system.")
    print ("""please login with your validated email and password 
            (x to cancel)
    """)

    while True:
        email = go_back("Enter your registered email: ")
        if email is None:
            return None
        password = go_back("Enter your password (x to cancel): ")
        if password is None:
            return None

        if not validate_email(email) or not validate_password(password):
            print("Incorrect email or password format")
            continue        

        student = validate_login(students, email, password)

        if student is not None:
            print(
                f"Login successful! Welcome {student.name} "
                f"(ID: {student.student_id})!"
            )
            return student

        else:
            print("Login failed. Please check your email and password.")
            print("Try again")