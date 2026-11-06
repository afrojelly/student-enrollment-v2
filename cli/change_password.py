from cli.utils import validate_password, go_back

def change_password(student, students, database):
    print("\nChange your password (enter x at any prompt to cancel).")

    while True:
        current_password = input("Enter your current password: ").strip()
        
        if current_password.lower() == "x":
            return go_back()
        
        if current_password == student.password:
            break

        print("Current password is incorrect. Please try again.")

    while True:
        new_password = input("Enter your new password: ").strip()
        
        if new_password.lower() == "x":
            return go_back()
        
        if not validate_password(new_password):
            print(
                "Invalid password. It must start with an uppercase letter, "
                "contain at least 5 letters, and end with at least 3 digits. "
                "Please try again."
            )
            continue

        confirm_password = input("Confirm your new password (x to cancel): ").strip()
        if confirm_password.lower() == "x":
            return go_back()

        if new_password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue

        student.password = new_password
        database.save_student(students)

        print(
            "Password changed successfully. \n"
            "Please use your new password the next time you log in."
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