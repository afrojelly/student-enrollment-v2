from cli.utils import colour, RED, GREEN, YELLOW, CYAN
# database
from cli.database import Database
# student
from cli import student_system
# admin
from cli import admin as admin

class UniApp:
    def __init__(self,data_file=None):
        self.database = Database() if data_file is None else Database(data_file)
        self.student_system = student_system.StudentSystem(self.database)
        self.admin_system = admin.AdminSystem(self.database)
    
    def university_system(self):
        while True:
            # print(colour("\nUniversity System", CYAN))
            # print(colour("(A)dmin", CYAN))
            # print(colour("(S)tudent", CYAN))
            # print(colour("(X)", CYAN))
            choice = input(colour("University System, (A)dmin, (S)tudent, or X: ", CYAN)).upper()

            if choice == 'A': 
                self.admin_system.admin_system()
            elif choice == 'S':
                self.student_system.student_system()
            elif choice == 'X':
                print(colour("\tThank you. Goodbye!", YELLOW))
                break
            else:
                print(colour("\tInvalid. Please try again.", RED))