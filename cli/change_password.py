from cli.utils import validate_password, go_back


def change_password(student, students, database):
    print("\nWould you like to change your password?. (x to cancel)")
    while True: #retain the existing identity cheack
        current_password = go_back("For Validation, Enter your current password: ")
        
        if current_password is None:
            return
        
        if current_password == student.password:
            break  #varify successful, proceed to change password
        else:
            print("Failed Verification. Please try again.")

#password validation and confirmation => validation function is called from registration.py
    while True:
        new_password = go_back("Enter your new password: ")
        
        if new_password is None:
            print("Password change cancelled.")
            return
        
        if not validate_password(new_password):
            print("""Wrong access. Please follow the password format.
            Password required
            - Must start with an Uppercase Letter
            - Contain at least 5-letter
            - followed by at least 3-digit Please try again.""")
            continue

        confirm_password = go_back("Confirm your new password: ")

        if confirm_password is None:
            print("Password change cancelled.")
            return

        if new_password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue

        student.password = new_password
        database.save_student(students) #changed password will be saved in the database

        print ("""Password changed successfully! 
        Please use your new password the next time you log in.""")
        return  # Exit the function after changing the password -> back to the subject enrolment system

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