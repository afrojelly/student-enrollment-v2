import registration 
import login 
import subject_enrolment 

#The Student subsystem menu, which includes login and registration functionalities for students.
class StudentSystem:
    def __init__(self,database):
        self.database = database
        self.students = self.database.loadStudents()

    def studentSystem(self):
        while True: 
            print 
            print("\nWelcome to the Student System. Please choose an option:")
            print(" (l) login")
            print(" (r) register")
            print(" (x) exit")

            choice = input("Enter your choice (l-r-x): ").lower()

            if choice == 'l':
                self.loginStudent()

            elif choice == 'r':
                self.registerStudent()

            elif choice == 'x':
                print("Exiting the Student System.")
                break

            else:
                print("Invalid. Please try again.")

    #Student system functionality.
    def registerStudent(self):         
        self.students = self.database.loadStudents() # Refresh records in case Admin has removed or cleared students.
        self.students = registration.registerStudent(
            self.students,
            self.database
        )

    def loginStudent(self):
        self.students = self.database.loadStudents()
        student = login.loginStudent(self.students)

        if student is None:
            return None
        
        if student is not None: # login에 불러온 student data -> enrolment system에서 불러옴 

            subject_enrolment.subjectEnrolmentSystem( 
                student, 
                self.students,
                self.database
                )
            return student
