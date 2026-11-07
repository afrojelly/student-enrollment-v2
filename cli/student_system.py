from cli.utils import colour, RED, GREEN, YELLOW, CYAN
from cli import student_registration
from cli import student_login
from cli import subject_enrolment 

class StudentSystem:
    def __init__(self,database):
        self.database = database
        self.students = self.database.load_students()

    def student_system(self):
        while True: 
            print(colour("\nWelcome to the Student System. Please choose an option:", CYAN))
            print(colour(" \t(l) login", CYAN))
            print(colour(" \t(r) register", CYAN))
            print(colour(" \t(x) exit", CYAN))

            choice = input(colour("\tEnter your choice (l-r-x): ", CYAN)).lower()

            if choice == 'l':
                self.login_student()
            elif choice == 'r':
                self.register_student()
            elif choice == 'x':
                print(colour("Exiting the Student System.", YELLOW))
                break
            else:
                print(colour("Invalid. Please try again.", RED))

    #Student system functionality.
    def register_student(self):
        self.students = self.database.load_students() # Refresh records in case Admin has removed or cleared students.
        self.students = student_registration.register_student(
            self.students,
            self.database
        )

    def login_student(self):
        self.students = self.database.load_students()
        student = student_login.login_student(self.students)

        if student is None:
            return None
        
        if student is not None: # login에 불러온 student data -> enrolment system에서 불러옴 

            subject_enrolment.subject_enrolment_system(
                student, 
                self.students,
                self.database
                )
            return student
