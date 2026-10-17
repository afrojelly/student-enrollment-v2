
import random #student ID generation
import re #email and password validation


from cli.student import Student


def registerStudent(students, database):       
    print("\n Welcome to the Student Registration System")
    while True:
        name = input("Enter your name: ") 
        if name:
            break
        else:
            print("Wrong access. Name cannot be empty. Please try again.")
            

    while True:
        email = input("Enter your email, following the format (firstname.lastname@university.com): ")  # actioned. Todo: firstname.lastname@university.com
        if validateEmail(email):

#email 중복체크? 
            existingEmails = {student.email for student in students}
            if email in existingEmails:
                print("This email is already registered. Please login or try another email.")
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
        if validatePassword(password):
            break
        else:
            print("""Wrong access. Please follow the password format.
            Password required
            - Must start with anUppercase Letter
            - Contain at least 5-letter
            - Contain at least 3-digit Please try again.""")

    studentId = generateStudentId(students)
    if studentId is None: 
        return students
##
    student = Student(name, email, password, studentId)
    newStudents = students+[student]

    database.saveStudent(newStudents)
  
    print("""Registration successful!, 
    please back to the student system and login with your email and password.""")
    print(f"Your student ID is: {student.studentId}")

    return newStudents #memory uptodate. return the updated list 

     
#validation for email and password format
def validateEmail(email): #email  #  actioned. Todo: email format: firstname.lastname@university.com  # 현재 특수문자 입력이 허용돼서 아이디 부분 "문자.문자" 형식만 입력 가능하도록 validation 수정 => actioned! 
    pattern = r"[A-Za-z]+\.[A-Za-z]+@university\.com"
    return bool(re.fullmatch(pattern, email))
#currently register multiple accounts with the same email address. Since we only have  pattern validation right now, should i add a duplicate email check before completing the registration ?  


def validatePassword(password): #password  #  actioned. Todo: password format이 현재는 대문자 + 영문4글자 + 숫자3자리로 고정되어있는데, 대문자 시작 부분만 고정하고 뒤에는 영문, 숫자 입력 순서 상관없이 가능하도록 수정 필요 => actioned! 
    pattern = r"[A-Z][A-Za-z0-9]*"
    return (
        bool(re.fullmatch(pattern,password))
        and sum(c.isalpha() for c in password) >= 5
        and sum(c.isdigit() for c in password) >= 3
        )
    
    
#Auto-student ID generation 
def generateStudentId(students):
    existingIds = {student.studentId for student in students}
    while True: 
        studentID = str(random.randint(1, 999999)).zfill(6)
        if studentID not in existingIds:
            return studentID
#만약 999999까지 다 차면 어떻게 되나요? 
# actioned 에러 처리 하면 됩니다!
# "All available student IDs have been used. A new student ID cannot be generated. Please contact the administrator."
# 이런식으로 message를 띄우고, 시스템 시작 화면으로 돌아가게 하면 될 것 같아요.
        if len(existingIds) > 999999: # if len();  used for execute code based on the number of items in a collection
            print ("""
            All available student IDs have been used
            A new student ID cannot be generated.
            Please contact the administrator""")


