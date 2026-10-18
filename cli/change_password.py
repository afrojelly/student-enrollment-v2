from cli.student_registration import validatePassword



#actioned. original password validation function needed? -튜터가 말했던 것 같은데.....
# ; before changing the password, the user enter the original password to verify their identity. 

def changePassword(student, students, database):
    print("\nWould you like to change your password?.")
    while True:
        currentPassword = input("Enter your current password and validate: ")
        if currentPassword == student.password:
            break  # exit loop, after validation of the current password
        else:
            print("Failed Verification. Please try again.")


#password validation and confirmation => validation function is called from registration.py
    while True:
        newPassword = input("Enter your new password: ")

        if not validatePassword(newPassword):
            print("""Wrong access. Please follow the password format.
            Password required
            - Must start with an Uppercase Letter
            - Contain at least 5-letter
            - Contain at least 3-digit Please try again.""")
            continue

        confirmPassword = input("Confirm your new password: ")
        if newPassword != confirmPassword:
            print("Passwords do not match. Please try again.")
            continue
#newPassword !=originalPassword => check if the new password is the same as the original password.
#필요한가?
        student.password = newPassword
        database.saveStudent(students) #changed password will be saved in the database

        print ("""Password changed successfully! 
        Please use your new password the next time you log in.""")
        return  # Exit the function after changing the password -> back to the subject enrolment system




def verifyPassword(student,currentPassword):
    return currentPassword == student.password


# Validate and save a new password
def updatePassword(student, students, database, newPassword, confirmPassword):

    if not validatePassword(newPassword):
        return "invalid"

    if newPassword != confirmPassword:
        return "mismatch"

    oldPassword = student.password
    student.password = newPassword

    try:
        database.saveStudent(students)
    except OSError:
        student.password = oldPassword
        return "saveError"

    return "success"