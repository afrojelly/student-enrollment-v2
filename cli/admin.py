from cli.utils import is_valid_student_id

class AdminSystem:
    def __init__(self, database):
        self.database = database
        self.students = self.database.load_students()

    def admin_system(self):
        while True:
            print("\n Welcome to the Admin System. Please choose a following option:")
            print(" (S) Show all students")
            print(" (G) Group students by grade")
            print(" (P) Partition students by pass/fail")
            print(" (R) Remove student")
            print(" (C) Clear database")
            print(" (X) Exit")

            choice = input("Choose an option (S/G/P/R/C/X): ").strip().upper()

            if choice == 'S':
                self.show_students_all()
            elif choice == 'G':
                self.group_students_by_grade()
            elif choice == 'P':
                self.partition_students_by_pass_fail()
            elif choice == 'R':
                self.remove_student()
            elif choice == 'C':
                self.clear_student()
            elif choice == 'X':
                print("Exiting the Admin System.")
                break
            else:
                print("Invalid. Please try again.")

    def show_students_all(self):
        self.students = self.database.load_students()

        if not self.students:
            print("No students registered.")
            return
        
        print("\n--- Student List ---")
        for student in self.students:
            print(f"{student.name} ({student.student_id}) / Email: {student.email}")

    def group_students_by_grade(self):
        self.students = self.database.load_students()

        if not self.students:
            print("No students registered.")
            return

        grade_groups = {
            "HD": [],
            "D": [],
            "C": [],
            "P": [],
            "Z": [],
        }
        students_without_subjects = []

        for student in self.students:
            average_mark = self.get_average_mark(student.subjects)

            if average_mark is None:
                students_without_subjects.append(student)
                continue

            grade = self.get_grade(average_mark)
            grade_groups[grade].append((student, average_mark))

        for grade, students in grade_groups.items():
            print(f"\n--- {grade} ---")
            if not students:
                print("No students in this grade.")
                continue

            for student, average_mark in students:
                print(
                    f"{student.name} ({student.student_id}) "
                    f"- Grade: {grade}, Average Mark: {average_mark:.2f}"
                )

        if students_without_subjects:
            print("\n--- No Subjects ---")
            for student in students_without_subjects:
                print(f"{student.name} ({student.student_id})")

    def partition_students_by_pass_fail(self):
        self.students = self.database.load_students()

        if not self.students:
            print("No students registered.")
            return

        pass_group = []
        fail_group = []
        students_without_subjects = []

        for student in self.students:
            average_mark = self.get_average_mark(student.subjects)

            if average_mark is None:
                students_without_subjects.append(student)
                continue

            grade = self.get_grade(average_mark)
            result = (student, grade, average_mark)

            if average_mark >= 50:
                pass_group.append(result)
            else:
                fail_group.append(result)

        if pass_group:
            print("\n--- PASS ---")
            for student, grade, average_mark in pass_group:
                print(
                    f"{student.name} ({student.student_id}) "
                    f"- Grade: {grade}, Average Mark: {average_mark:.2f}"
                )

        if fail_group:
            print("\n--- FAIL ---")
            for student, grade, average_mark in fail_group:
                print(
                    f"{student.name} ({student.student_id}) "
                    f"- Grade: {grade}, Average Mark: {average_mark:.2f}"
                )

        if students_without_subjects:
            print("\n--- No Subjects ---")
            for student in students_without_subjects:
                print(f"{student.name} ({student.student_id})")

    def remove_student(self):
        while True:
            input_id = input(
                "Enter the 6-digit student ID to remove: "
            ).strip()

            if not is_valid_student_id(input_id):
                print("Invalid student ID. Please enter a 6-digit ID.")
                continue

            student = self.database.get_student(input_id)
            if student is None:
                print(f"No student found with ID {input_id}. Please try again.")
                continue

            break

        confirmation = input(f"Are you sure you want to delete {student.name} ({student.student_id})? (Y/N): ").strip().upper()

        if confirmation == 'Y':
            if self.database.delete_student(student.student_id):
                print(f"Student {student.name} ({student.student_id}) has been deleted.")
            else:
                print(f"Student with ID {student.student_id} could not be found.")
        else:
            print("Operation cancelled.")

    def clear_student(self):
        confirmation = input("This will permanently delete all student records. Are you sure? (Y/N): ").strip().upper()
        if confirmation == 'Y':
            self.database.clear_students()
            print("All student data has been cleared.") 
        else:
            print("Operation cancelled.")

    def get_average_mark(self, subjects):
        if len(subjects) == 0:
            return None

        total = sum(subject["mark"] for subject in subjects)
        return total / len(subjects)

    def get_grade(self, average_mark):
        if average_mark >= 85:
            grade = "HD"
        elif average_mark >= 75:
            grade = "D"
        elif average_mark >= 65:
            grade = "C"
        elif average_mark >= 50:
            grade = "P"
        else:
            grade = "Z"

        return grade


