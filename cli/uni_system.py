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
            print(colour("\nWelcome to the University System. please choose a following option", CYAN))
            print(colour(" \t(A) Admin", CYAN))
            print(colour(" \t(S) Student", CYAN))
            print(colour(" \t(X) Exit", CYAN))
            choice = input(colour(" \tEnter your choice (A-S-X): ", CYAN)).upper()

            if choice == 'A': 
                self.admin_system.admin_system()
            elif choice == 'S':
                self.student_system.student_system()
            elif choice == 'X':
                print(colour("\tExiting the UniApp. Goodbye!", YELLOW))
                break
            else:
                print(colour("\tInvalid. Please try again.", RED))