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
            print("\nWelcome to the University System. please choose a following option")
            print(" (A) Admin")
            print(" (S) Student")
            print(" (X) Exit")
            choice = input("Enter your choice (A-S-X): ").upper()

            if choice == 'A': 
                self.admin_system.admin_system()
            elif choice == 'S':
                self.student_system.student_system()
            elif choice == 'X':
                print("Exiting the UniApp. Goodbye!")
                break
            else:
                print("Invalid. Please try again.")