from cli.utils import colour, RED, GREEN, YELLOW, CYAN
from cli.utils import get_grade, is_valid_student_id

class AdminSystem:
    def __init__(self, database):
        self.database = database

    def admin_system(self):
        while True:
            print(colour("\tAdmin System", CYAN))
            print(colour("\t(s) Show all students", CYAN))
            print(colour("\t(g) Group students by grade", CYAN))
            print(colour("\t(p) Show pass/fail results", CYAN))
            print(colour("\t(r) Remove student", CYAN))
            print(colour("\t(c) Clear database", CYAN))
            print(colour("\t(x) Exit", CYAN))
            choice = input(colour("\tPlease choose an option (s/g/p/r/c/x): ", CYAN)).strip().lower()
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
                break
            else:
                print(colour("\tInvalid. Please try again.", RED))

    def show_students_all(self):
        students = self.database.load_students()

        print(colour("\tStudent List", YELLOW))

        if not students:
            print("\t\t< Nothing to Display >")
            return
        

        for student in students:
            print(f"\t{student.name} :: {student.student_id} --> Email: {student.email}")

    def group_students_by_grade(self):
        students = self.database.load_students()

        print(colour("\tGrade Grouping", YELLOW))

        if not students:
            print("\t\t< Nothing to Display >")
            return

        grade_groups = {
            "HD": [],
            "D": [],
            "C": [],
            "P": [],
            "Z": [],
        }

        for student in students:
            average_mark = student.average_mark

            if average_mark is None:
                continue

            grade = get_grade(average_mark)
            grade_groups[grade].append((student, average_mark))

        for grade, grade_students in grade_groups.items():
            if not grade_students:
                continue

            student_details = ", ".join(
                f"\n\t\t{student.name} :: ({student.student_id}) --> "
                f"GRADE: {grade} - MARK: {average_mark:.2f}"
                for student, average_mark in grade_students
            )
            print(f"\t{grade} --> [{student_details}\n\t]")

    def partition_students_by_pass_fail(self):
        students = self.database.load_students()

        print(colour("\tPASS/FAIL Partition", YELLOW))

        if not students:
            print("\t\t< Nothing to Display >")
            return

        pass_group = []
        fail_group = []

        for student in students:
            average_mark = student.average_mark

            if average_mark is None:
                continue

            grade = get_grade(average_mark)
            result = (student, grade, average_mark)

            if average_mark >= 50:
                pass_group.append(result)
            else:
                fail_group.append(result)

        students_pass = ", ".join(
            f"\n\t\t{student.name} :: ({student.student_id}) --> "
            f"GRADE: {grade} - MARK: {average_mark:.2f}"
            for student, grade, average_mark in pass_group
        )

        students_fail = ", ".join(
            f"\n\t\t{student.name} :: ({student.student_id}) --> "
            f"GRADE: {grade} - MARK: {average_mark:.2f}"
            for student, grade, average_mark in fail_group
        )

        if pass_group:
            print(f"\tPASS --> [{students_pass}\n\t]")
        else:
            print("\tPASS --> []")

        if fail_group:
            print(f"\tFAIL --> [{students_fail}\n\t]")
        else:
            print("\tFAIL --> []")

    def remove_student(self):
        input_id = input("\tRemove by ID: ").strip()

        if input_id.lower() == "x":
            return

        # if not is_valid_student_id(input_id):
        #     print("Invalid student ID. Please enter a 6-digit ID.")
        #     continue

        student = self.database.get_student(input_id)
        if student is None:
            print(colour(f"\tStudent {input_id} does not exist", RED))
            return

        if self.database.delete_student(student.student_id):
            print(colour(f"\tRemoving student {student.student_id} Account", YELLOW))
        else:
            print(colour(f"\tFailed to remove student {student.student_id}", RED))

    def clear_students(self):
        print(colour("\tClearing students database", YELLOW))

        input_value = input(colour("\tAre you sure you want to clear the database (Y)ES/(N)O: ", RED)).strip().upper()
        if input_value == "Y":
            self.database.clear_students()
            print(colour("\tStudent data cleared", YELLOW))
        elif input_value == "N":
            return