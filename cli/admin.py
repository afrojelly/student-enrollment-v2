from cli.utils import isValidStudentId

class AdminSystem:
    def __init__(self, database):
        self.database = database
        self.students = self.database.loadStudents()

    def adminSystem(self):
        while True:
            print("\n Welcome to the Admin System. Please choose a following option:")
            print(" (V) View all students")
            print(" (G) View students by grade")
            print(" (P) View students categorised by pass/fail")
            print(" (D) Delete one student by ID")
            print(" (C) Clear all student data")
            print(" (X) Exit")

            choice = input("Choose an option (V/G/P/D/C/X): ").strip().upper()

            if choice == 'V':
                self.veiwStudentsAll()
            elif choice == 'G':
                self.viewStudentsByGrade()
            elif choice == 'P':
                self.viewStudentsByPassFail()
            elif choice == 'D':
                self.deleteStudent()
            elif choice == 'C':
                self.clearStudent()
            elif choice == 'X':
                print("Exiting the Admin System.")
                break
            else:
                print("Invalid. Please try again.")

    def veiwStudentsAll(self):
        self.students = self.database.loadStudents()

        if not self.students:
            print("No students registered.")
            return
        
        print("\n--- Student List ---")
        for student in self.students:
            print(f"{student.name} ({student.studentId}) / Email: {student.email}")
            # print(
            #     # f"ID: {student.studentId}, "
            #     # f"Name: {student.name}, "
            #     # f"Email: {student.email}, "
            #     # f"Subjects: {student.subjects}, "
            # )

    def viewStudentsByGrade(self):
        self.students = self.database.loadStudents()

        if not self.students:
            print("No students registered.")
            return

        gradeGroups = {
            "HD": [],
            "D": [],
            "C": [],
            "P": [],
            "Z": [],
        }
        studentsWithoutSubjects = []


        for student in self.students:
            averageMark = self.getAverageMark(student.subjects)

            if averageMark is None:
                studentsWithoutSubjects.append(student)
                continue

            grade = self.getGrade(averageMark)
            gradeGroups[grade].append((student, averageMark))

        for grade, students in gradeGroups.items():
            print(f"\n--- {grade} ---")
            if not students:
                print("No students in this grade.")
                continue

            for student, averageMark in students:
                print(
                    f"{student.name} ({student.studentId}) "
                    f"- Grade: {grade}, Average Mark: {averageMark:.2f}"
                )

        if studentsWithoutSubjects:
            print("\n--- No Subjects ---")
            for student in studentsWithoutSubjects:
                print(f"{student.name} ({student.studentId})")

    def viewStudentsByPassFail(self):
        self.students = self.database.loadStudents()

        if not self.students:
            print("No students registered.")
            return

        passGroup = []
        failGroup = []
        studentsWithoutSubjects = []

        for student in self.students:
            averageMark = self.getAverageMark(student.subjects)

            if averageMark is None:
                studentsWithoutSubjects.append(student)
                continue

            grade = self.getGrade(averageMark)
            result = (student, grade, averageMark)

            if averageMark >= 50:
                passGroup.append(result)
            else:
                failGroup.append(result)

        if passGroup:
            print("\n--- PASS ---")
            for student, grade, averageMark in passGroup:
                print(
                    f"{student.name} ({student.studentId}) "
                    f"- Grade: {grade}, Average Mark: {averageMark:.2f}"
                )

        if failGroup:
            print("\n--- FAIL ---")
            for student, grade, averageMark in failGroup:
                print(
                    f"{student.name} ({student.studentId}) "
                    f"- Grade: {grade}, Average Mark: {averageMark:.2f}"
                )

        if studentsWithoutSubjects:
            print("\n--- No Subjects ---")
            for student in studentsWithoutSubjects:
                print(f"{student.name} ({student.studentId})")  

    def deleteStudent(self):
        inputId = input("Enter the 6-digit student ID to delete: ")

        # verify entered studentId correctly.(6-digits, only number allowed)
        if not isValidStudentId(inputId):
            print("Invalid student ID. Please enter a 6-digit ID.")
            return

        # finding matching student
        student = self.database.getStudent(inputId)
        if student is None:
            print(f"No student found with ID {inputId}.")
            return

        # Todo: ask confirmation question 할까말까?
        confirmation = input(f"Are you sure you want to delete {student.name} ({student.studentId})? (Y/N): ").strip().upper()

        if confirmation == 'Y':
            if self.database.deleteStudent(student.studentId):
                print(f"Student {student.name} ({student.studentId}) has been deleted.")
            else:
                print(f"Student with ID {student.studentId} could not be found.")
        else:
            print("Operation cancelled.")

    def clearStudent(self):
        confirmation = input("This will permanently delete all student records. Are you sure? (Y/N): ").strip().upper()
        if confirmation == 'Y':
            self.database.clearStudents()
            print("All student data has been cleared.") 
        else:
            print("Operation cancelled.")


    def getAverageMark(self, subjects):
        if len(subjects) == 0:
            return None

        total = sum(subject["mark"] for subject in subjects)
        return total / len(subjects)

    def getGrade(self, mark):
        if mark >= 85:
            grade = "HD"
        elif mark >= 75:
            grade = "D"
        elif mark >= 65:
            grade = "C"
        elif mark >= 50:
            grade = "P"
        else:
            grade = "Z"

        return grade
