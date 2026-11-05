
import random #student ID generation

from cli.student import Student

from cli.utils import validate_email, validate_password, go_back



def register_student(students, database):
    print("\n Welcome to the Student Registration System (x to cancel)")
    while True:
        name = go_back("Enter your name: ")
        if name is None:
            return students

        name = name.strip()
        if name:
            break
        print("Name cannot be empty, try again")

    while True:
        email = go_back("Enter your email, following the format (firstname.lastname@university.com): ")  # actioned. Todo: firstname.lastname@university.com
        if email is None:
            return students

        if validate_email(email):

#email duplication check
            existing_emails = {student.email for student in students}
            if email in existing_emails:
                print("This email is already registered. Please try another email.")
                continue 
            break

        else:
            print("""Wrong access. Enter a valid email address
            firstname.lastname@university.com""")

    while True:
        password = go_back("Enter your password (Password123): ")
        if password is None:
            return students
        
        if validate_password(password):
            break
        else:
            print("""Wrong access. Please follow the password format.
            Password required
            - Must start with anUppercase Letter
            - Contain at least 5-letter
            - followed by at least 3-digit Please try again.""")

    student_id = generate_student_id(students)
    if student_id is None:
        return students

    student = Student(name, email, password, student_id)
    new_students = students+[student]

    database.save_student(new_students)

    print("""Registration successful!, 
    please login with your email and password.""")
    print(f"Your student ID is: {student.student_id}")

    return new_students #memory uptodate. return the updated list

#Auto-student ID generation 
def generate_student_id(students):
    existing_ids = {student.student_id for student in students}
    while True: 
        student_id = str(random.randint(1, 999999)).zfill(6)
        if student_id not in existing_ids:
            return student_id
        
#if 999,999 student IDs are already used, the system will not be able to generate a new ID. In that case, it will return None and print a message to contact the administrator.
        if len(existing_ids) >= 999999: # if len();  used for execute code based on the number of items in a collection
            print ("""
            All available student IDs have been used
            A new student ID cannot be generated.
            Please contact the administrator
            """)
            return None