#method: veiwAllStudents():void, organiseStudentByGrade():void, categoriseStudentsPassFail():void, clearStudentData():void 
#Regarding the data base remove; remove the data only=empting the file 
#Mark: how do we decide the pass/fail => return / Student average mark >=50; pass /<50; fail 
#Student remove; with the student ID 


class AdminSystem:
    def __init__(self, database):
        self.database = database
        self.students = self.database.loadStudents()

    def adminSystem(self):
        while True:
            print("\n Welcome to the Admin System. Please choose a following option:")
            print(" (V) View all students")
            print(" (O) Organise students by grade")
            print(" (C) Categorise students as pass/fail")
            print(" (R) Remove student by ID")
            print(" (L) Clear student data")
            print(" (X) Exit")
            choice = input("Enter your choice (V-O-C-R-L-X): ").upper()

            if choice == 'V':
                self.viewAllStudents()
            elif choice == 'O':
                self.organiseStudentByGrade()
            elif choice == 'C':
                self.categoriseStudentsPassFail()
            elif choice == 'R':
                self.removeStudentByID()
            elif choice == 'L':
                self.clearStudentData()
            elif choice == 'X':
                print("Exiting the Admin System.")
                break
            else:
                print("Invalid. Please try again.")

    def viewAllStudents(self):
        self.students = self.database.loadStudents()
        for student in self.students:
            print(
                f"ID: {student.studentId}, "
                f"Name: {student.name}, "
                f"Email: {student.email}, "
                f"Subjects: {student.subjects}, "
            )

    def organiseStudentByGrade(self):
        self.students = self.database.loadStudents()

        def get_average_mark(student):
            subjects = student.subjects

            if len(subjects) == 0:
                return -1

            total = sum(subject["mark"] for subject in subjects)
            return total / len(subjects)

        sorted_students = sorted(
            self.students,
            key=get_average_mark,
            reverse=True
        )

        for student in sorted_students:
            print(
                f"ID: {student.studentId}, "
                f"Name: {student.name}, "
                f"Email: {student.email}, "
                f"Subjects: {student.subjects}, "
            )

    def categoriseStudentsPassFail(self):
        self.students = self.database.loadStudents()
        for student in self.students:
            if student.average_mark >= 50: # this averageMark is the average mark of 4 subject, like the GPA, we wouldn't generate the mark for each subject, only scoring
                status = "Pass"
            else:
                status = "Fail"
            print(f"{student} - {status}")

    def clearStudentData(self):
        confirmation = input("Are you sure you want to clear all student data? (Y/N): ").upper()
        if confirmation == 'Y':
            self.database.clearStudentData()
            print("All student data has been cleared.")
        else:
            print("Operation cancelled.")