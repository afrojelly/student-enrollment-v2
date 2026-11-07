from cli.utils import colour, RED, GREEN, YELLOW, CYAN
from cli.utils import validate_password, go_back

def change_password(student, students, database):
    print(colour("\nChange password (enter x at any prompt to cancel).", CYAN))

    while True:
        current_password = input("\tValidate Current password  (x to cancel): ").strip()
        
        if current_password.lower() == "x":
            return go_back()
        
        if current_password == student.password:
            break

        print(colour("\tCurrent password is incorrect. Please try again.", RED))

    while True:
        new_password = input("\tNew password (x to cancel): ").strip()
        
        if new_password.lower() == "x":
            return go_back()
        
        if not validate_password(new_password):
            print(colour(
                "\tInvalid password. It must start with an uppercase letter, "  
                "\tcontain more than 5 letters, followed by at least 3 digits. "  
                "\tPlease try again.", RED)
            )
            continue

        confirm_password = input("\tConfirm new password (x to cancel): ").strip()
        if confirm_password.lower() == "x":
            return go_back()

        if new_password != confirm_password:
            print(colour("\tPasswords not match. Please try again.", RED))
            continue

        student.password = new_password
        database.save_student(students)

        print(colour(
            "\tPassword changed successfully. \n"
            "\tPlease use your new password the next time you log in.", GREEN)
        )
        return

def verify_password(student,current_password):
    return current_password == student.password

# Validate and save a new password
def update_password(student, students, database, new_password, confirm_password):
    if not validate_password(new_password):
        return "invalid"

    if new_password != confirm_password:
        return "mismatch"

    old_password = student.password
    student.password = new_password

    try:
        database.save_student(students)
    except OSError:
        student.password = old_password
        return "saveError"

    return "success"