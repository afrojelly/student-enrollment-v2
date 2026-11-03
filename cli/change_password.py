from cli.utils import validate_password



#actioned. original password validation function needed? -튜터가 말했던 것 같은데.....
# ; before changing the password, the user enter the original password to verify their identity. 

def change_password(student, students, database):
    print("\nWould you like to change your password?.")
    while True:
        current_password = input("Enter your current password and validate: ")
        if current_password == student.password:
            break  # exit loop, after validation of the current password
        else:
            print("Failed Verification. Please try again.")


#password validation and confirmation => validation function is called from registration.py
    while True:
        new_password = input("Enter your new password: ")

        if not validate_password(new_password):
            print("""Wrong access. Please follow the password format.
            Password required
            - Must start with an Uppercase Letter
            - Contain at least 5-letter
            - followed by at least 3-digit Please try again.""")
            continue

        confirm_password = input("Confirm your new password: ")
        if new_password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue
# new_password != original_password: check whether the new password differs.
#필요한가?
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