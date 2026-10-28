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
            print(" (R) Remove a student by ID")
            print(" (L) Clear all student data")
            print(" (X) Exit")
            choice = input("Enter your choice (V-O-C-R-L-X): ").upper().strip()

            if choice == 'V':
                self.veiwStudentsAll()
            elif choice == 'O':
                self.viewStudentsByGrade()
            elif choice == 'C':
                self.viewStudentsByPassFail()
            elif choice == 'R':
                self.deleteStudent()
            elif choice == 'L':
                self.clearStudent()
            elif choice == 'X':
                print("Exiting the Admin System.")
                break
            else:
                print("Invalid. Please try again.")

    def veiwStudentsAll(self):
        self.students = self.database.loadStudents()

        print("--- Student List ---")
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
        student = self.database.get_student(inputId)

        if student is None:
            print(f"No student found with ID {inputId}.")
        else:
            self.database.delete_student(inputId)
            print(f"Student with ID {inputId} has been removed.")
        
        # verify entered studentId correctly.(6-digits, only number allowed)
        
        # search the studentId from Students.data

        # If there is no matched studentId, return error message amd go back to menu.
        # otherwise, ask confirmation question.

        # If user say yes, delete the data of the student.
        # otherwise, return the message and go back to menu.
        

    def clearStudent(self):
        confirmation = input("This will permanently delete all student records. Are you sure? (Y/N): ").upper().strip()
        if confirmation == 'Y':
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
