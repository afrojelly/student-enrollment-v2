#exit page; go back to the before page; atm, don't have to have 
#def  exitOrLogin(string)
 #   value = input(string)
#
 #   if value.string() == "X":
  #      print ("Returning to the student system.")
   #     return None
    #return value 
def validateLogin(students, email, password):
    for student in students:
        if student.email == email and student.password == password:
            return student

    return None
def loginStudent(students):
    print("\nwelcome to the Student Login system.")
    print ("""please login with your validated email and password
    """)

    while True:
        email = input("Enter your registered email: ")
        password = input ("enter you password: ")

        for student in students:
            if student.email == email and student.password == password:
                print (f"login successful!, Welcome {student.name} (ID: {student.studentId})!")
                return student 
            
        #actioned. page는 student enrolment page로 넘어가게 해야함
        #=> 추가로 로그인 상태 유지할 수 있게 로그인 기록 기억 넣어야할까요? 
        #actioned. 어떻게 하는지 몰라서 좀 더 찾아봐야할 듯! student  
        #student informationn이 subject enrolment system으로 바로 전달될 수 있게 uni_systedml login에 불러오는 data를추초가했어요-uni_system.py에!

        print ("Login failed. please check your email and password.")
        print ("Try again")
        print ("or if you have not registered, exit and register first.")
