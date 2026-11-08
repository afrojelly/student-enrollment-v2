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
            print(colour("\tStudent System", CYAN))
            print(colour("\t(l)ogin", CYAN))
            print(colour("\t(r)egister", CYAN))
            print(colour("\t(x)", CYAN))

            choice = input(colour("\tPlease choose an option (l/r/x): ", CYAN)).lower()

            try:
                if choice == 'l':
                    self.login_student()
                elif choice == 'r':
                    self.register_student()
                elif choice == 'x':
                    print(colour("\tExiting the Student System.", YELLOW))
                    break
                else:
                    print(colour("\tInvalid. Please try again.", RED))
            except OSError as error:
                print(colour(str(error), RED))
    
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
        
        if student is not None:

            subject_enrolment.subject_enrolment_system(
                student, 
                self.students,
                self.database
                )
            return student
