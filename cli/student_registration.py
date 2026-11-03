
import random #student ID generation

from cli.student import Student

from cli.utils import validate_email
from cli.utils import validate_password


def register_student(students, database):
    print("\n Welcome to the Student Registration System")
    while True:
        name = input("Enter your name: ") 
        if name:
            break
        else:
            print("Wrong access. Name cannot be empty. Please try again.")
            

    while True:
        email = input("Enter your email, following the format (firstname.lastname@university.com): ")  # actioned. Todo: firstname.lastname@university.com
        if validate_email(email):

#email 중복체크? 
            existing_emails = {student.email for student in students}
            if email in existing_emails:
                print("This email is already registered. Please try another email.")
                continue 
#중복체크      
# just block the registration if the email is already registered will be enough
# 근데 동명이인이 있으면 어떻게 하죠.....? 우리학교 시스템처럼 뒤에 숫자같은 구분문자/suffix 를 자동으로 붙이는 식으로 해야할까요....?       =>  
            break

        else:
            print("""Wrong access. Enter a valid email address
            firstname.lastname@university.com""")

    while True:
        password = input("Enter your password (Password123): ")
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
#만약 999999까지 다 차면 어떻게 되나요? 
# actioned 에러 처리 하면 됩니다!
# "All available student IDs have been used. A new student ID cannot be generated. Please contact the administrator."
# 이런식으로 message를 띄우고, 시스템 시작 화면으로 돌아가게 하면 될 것 같아요.
        if len(existing_ids) > 999999: # if len();  used for execute code based on the number of items in a collection
            print ("""
            All available student IDs have been used
            A new student ID cannot be generated.
            Please contact the administrator""")