import json
import logging
from pathlib import Path

from cli.student import Student


class Database: 
    def __init__(self, data_file = None):
        self.data_file=(
            Path(data_file)
            if data_file is not None
            else Path(__file__).with_name("students.data") #data base; student data file; generated automatically 
        )
        self.read_error = False
        if not self.data_file.exists():
            try:
                self.save_student([])
            except OSError as error:
                logging.error("Initialization error: %s", error)
                self.read_error = True

    # Save student information 
    def save_student(self,students_info):
        if self.read_error:
            error = OSError("Cannot save: repair the student data file first.")
            logging.error("%s", error)
            raise error

        try:
            data = []

            for student in students_info:
                data.append(student.to_record())

            # Generate a temporary file before replacing data_file.
            temp_file = self.data_file.with_name(
                self.data_file.name + ".temp"
            )
            with temp_file.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
            temp_file.replace(self.data_file)
        except OSError as error:
            logging.error("Writing error: %s", error)
            raise

    # Bring the student data as the reader mode 
    def load_students(self):
        try:
            with self.data_file.open("r", encoding="utf-8") as file:
                content = file.read().strip()
            if not content:
                self.read_error = False
                return []

            data = json.loads(content)
            if not isinstance(data, list):
                raise ValueError("Student data must be a list.")

            students_info = []
            for item in data:
                if not isinstance(item, dict):
                    raise ValueError("Invalid student record.")
                student = Student.from_record(item)
                students_info.append(student)

            self.read_error = False
            return students_info
        except FileNotFoundError as error:
            logging.error("File not found: %s", error)
        except OSError as error:
            logging.error("Reading error: %s", error)
        except json.JSONDecodeError as error:
            logging.error("Invalid JSON data: %s", error)
        except (KeyError, TypeError, ValueError) as error:
            logging.error("Invalid student data: %s", error)

        self.read_error = True
        print(
            "\033[31mStudent data file is corrupted or unreadable. "
            "Please repair the file before saving changes.\033[0m"
        )
        return []

    # Delete student by id
    def delete_student(self, student_id):
        students = self.load_students()

        for student in students:
            if student.student_id == student_id:
                students.remove(student)
                self.save_student(students)
                return True

        return False

    # Clear all students
    def clear_students(self):
        # Keep the empty list as valid JSON so load_students() can read it.
        self.save_student([])

    # Get student by id
    def get_student(self, student_id):
        students = self.load_students()

        for student in students:
            if student.student_id == student_id:
                return student

        return None