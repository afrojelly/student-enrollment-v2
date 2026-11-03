import json
from pathlib import Path

from cli.student import Student

class Database: 
    def __init__(self, data_file = None):
        self.data_file=(
            Path(data_file)
            if data_file is not None
            else Path(__file__).with_name("Students.data") #data base; student data file; generated automatically 
        )
        if not self.data_file.exists():
            self.save_student([])

    #save Student Information 
    def save_student(self,students_info):
        data =[]

        for student in students_info:
            data.append(student.to_record())

        # Generate a temporary file before replacing data_file.
        temp_file =self.data_file.with_name(
            self.data_file.name + ".temp"
        )
        with temp_file.open ("w",encoding ="utf-8") as file:
            json.dump(data, file, indent=4)
        temp_file.replace(self.data_file)

    # bring the student data as the reader mode 
    def load_students(self):
        with self.data_file.open("r", encoding="utf-8") as file:
            data = json.load(file)

        students_info = []
        for item in data:
            student = Student.from_record(item)
            students_info.append(student)

        return students_info

    def delete_student(self, student_id):
        students = self.load_students()

        for student in students:
            if student.student_id == student_id:
                students.remove(student)
                self.save_student(students)
                return True

        return False

    def clear_students(self):
        # Keep the empty list as valid JSON so load_students() can read it.
        self.save_student([])

    # get student by id
    def get_student(self, student_id):
        students = self.load_students()

        for student in students:
            if student.student_id == student_id:
                return student

        return None