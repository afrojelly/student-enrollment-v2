from cli import student_registration
from cli import student_login
from cli import subject_enrolment 

class StudentSystem:
    def __init__(self,database):
        self.database = database
        self.students = self.database.load_students()

    def student_system(self):
        while True: 
            print("\nWelcome to the Student System. Please choose an option:")
            print(" (l) login")
            print(" (r) register")
            print(" (x) exit")

            choice = input("Enter your choice (l-r-x): ").lower()

            if choice == 'l':
                self.login_student()
            elif choice == 'r':
                self.register_student()
            elif choice == 'x':
                print("Exiting the Student System.")
                break
            else:
                print("Invalid. Please try again.")

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
