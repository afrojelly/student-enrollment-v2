
# database
from cli.database import Database
# student
from cli import student_system
# admin
from cli import admin as admin


class UniApp:
#setting the database, initiation. 
    def __init__(self,data_file=None):
        self.database = Database() if data_file is None else Database(data_file)
        self.student_system = student_system.StudentSystem(self.database)
        self.admin_system = admin.AdminSystem(self.database)
    
#University System requiremnt, choosing the subsystem class. 
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


#  각각의 기능을 다른 파일로 빼서,  student, admin system에서 각각의 def를 선택시에 불러오는 방향으로 파일을 분리하는게 좋을 것 같습니다. 
#Student Registration functionality.


#actioned. login 후 student page;' enrolment page로 가게 해야합니다; here need to be connected to the subject enrolment system 
# #done! 


        