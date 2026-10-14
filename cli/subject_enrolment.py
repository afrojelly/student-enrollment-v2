from change_password import changePassword

def subjectEnrolmentSystem(student, students, database):
    while True:
        print(f"\nWelcome to the Subject Enrolment System , {student.name}. Please choose a following option: ")
        print ("(c) change password")
        print( "(e) enrol in a subject")
        print ("(r) remove a subject")
        print ("(s) show enrolled subjects")
        print ("(x) exit")
        choice = input("Enter your choice (c-e-r-s-x): ").lower()
#여기에 choice에 따라 각각의 기능을정의하고 def를 불러오는 방식으로 구현하면 될 것 같습니다아앙
#change password def는 change_password.py에 따로 빼서 정의해서/
# enrol, remove, show def는 subject_enrolment.py(현재파일)에 정의해도 될 것 같아요 but up to you! :)


        if choice == 'c':
            changePassword(student, students, database)  


        elif choice == 'x':
            print("Exiting the Subject Enrolment System.")
            break

        
# actioned. changePassword import "from change_password import changePassword"


#subject enrolment; creating the subject list , length of 5 (limit) -> if more than 4, showing error -> if student tr more thant this, showing error - reaching the max num of subject  




#  #Subject remove: How should it work. -> enter the subject ID->system find the subject -> remove from the list -> update -> display 