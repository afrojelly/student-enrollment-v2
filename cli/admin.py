from cli.utils import get_grade, is_valid_student_id

class AdminSystem:
    def __init__(self, database):
        self.database = database

    def admin_system(self):
        while True:
            print("\nWelcome to the Admin System. Please choose an option:")
            print(" (s) Show all students")
            print(" (g) Group students by grade")
            print(" (p) Show pass/fail results")
            print(" (r) Remove student")
            print(" (c) Clear database")
            print(" (x) Exit")

            choice = input("Choose an option (s/g/p/r/c/x): ").strip().lower()

            if choice == "s":
                self.show_students_all()
            elif choice == "g":
                self.group_students_by_grade()
            elif choice == "p":
                self.partition_students_by_pass_fail()
            elif choice == "r":
                self.remove_student()
            elif choice == "c":
                self.clear_students()
            elif choice == "x":
                print("Exiting the Admin System.")
                break
            else:
                print("Invalid. Please try again.")

    def show_students_all(self):
        students = self.database.load_students()

        if not students:
            print("No students registered.")
            return
        
        print("\n--- Student List ---")

        for student in students:
            print(f"{student.name} ({student.student_id}) / Email: {student.email}")

    def group_students_by_grade(self):
        students = self.database.load_students()

        if not students:
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

        for student in students:
            average_mark = self._get_average_mark(student.subjects)

            if average_mark is None:
                students_without_subjects.append(student)
                continue

            grade = get_grade(average_mark)
            grade_groups[grade].append((student, average_mark))

        for grade, grade_students in grade_groups.items():
            print(f"\n--- {grade} ---")
            if not grade_students:
                print("No students in this grade.")
                continue

            for student, average_mark in grade_students:
                print(
                    f"{student.name} ({student.student_id}) "
                    f"- Grade: {grade}, Average Mark: {average_mark:.2f}"
                )

        if students_without_subjects:
            print("\n--- No Subjects ---")
            for student in students_without_subjects:
                print(f"{student.name} ({student.student_id})")

    def partition_students_by_pass_fail(self):
        students = self.database.load_students()

        if not students:
            print("No students registered.")
            return

        pass_group = []
        fail_group = []
        students_without_subjects = []

        for student in students:
            average_mark = self._get_average_mark(student.subjects)

            if average_mark is None:
                students_without_subjects.append(student)
                continue

            grade = get_grade(average_mark)
            result = (student, grade, average_mark)

            if average_mark >= 50:
                pass_group.append(result)
            else:
                fail_group.append(result)

        print("\n--- PASS ---")
        if not pass_group:
            print("No students passed.")

        for student, grade, average_mark in pass_group:
            print(
                f"{student.name} ({student.student_id}) "
                f"- Grade: {grade}, Average Mark: {average_mark:.2f}"
            )

        print("\n--- FAIL ---")
        if not fail_group:
            print("No students failed.")

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
                "Enter the 6-digit student ID to remove (x to cancel): "
            ).strip()

            if input_id.lower() == "x":
                print("Operation cancelled.")
                return

            if not is_valid_student_id(input_id):
                print("Invalid student ID. Please enter a 6-digit ID.")
                continue

            student = self.database.get_student(input_id)
            if student is None:
                print(f"No student found with ID {input_id}. Please try again.")
                continue

            break

        confirm_statement = f"Are you sure you want to delete {student.name} ({student.student_id})? (y/n): "
        if self._confirm_action(confirm_statement):
            if self.database.delete_student(student.student_id):
                print(f"Student {student.name} ({student.student_id}) has been deleted.")
            else:
                print(f"Student with ID {student.student_id} could not be found.")
        else:
            print("Operation cancelled.")

    def clear_students(self):
        confirm_statement = "This will permanently delete all student records. Are you sure? (y/n): "
        if self._confirm_action(confirm_statement):
            self.database.clear_students()
            print("All student data has been cleared.")
        else:
            print("Operation cancelled.")

    def _confirm_action(self, prompt):
        while True:
            confirmation = input(prompt).strip().lower()
            if confirmation == "y":
                return True
            if confirmation == "n":
                return False
            print("Invalid choice. Please enter y or n.")

    def _get_average_mark(self, subjects):
        if len(subjects) == 0:
            return None

        total = sum(subject["mark"] for subject in subjects)
        return total / len(subjects)