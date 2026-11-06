import random

class Subject:
    def __init__(self, student):
        self.subject_id = self.generate_subject_id(student)
        self.mark = self.generate_mark()      # 305: mark generated automatically
        self.grade = self.calculate_grade()   # 306: grade calculated from the mark

    # random subject ID
    def generate_subject_id(self, student):
        existing_ids = {subject["id"] for subject in student.subjects}
        while True:
            subject_id = str(random.randint(1, 999)).zfill(3)
            if subject_id not in existing_ids:
                return subject_id

    # random mark between 25 and 100
    def generate_mark(self):
        return random.randint(25, 100)

    # Use the same grading rule as AdminSystem.get_grade().
    def calculate_grade(self):
        if self.mark >= 85:
            return "HD"
        elif self.mark >= 75:
            return "D"
        elif self.mark >= 65:
            return "C"
        elif self.mark >= 50:
            return "P"
        else:
            return "Z"

    # Subject object -> dictionary (Students.data format)
    def to_record(self):
        return {
            "id": self.subject_id,
            "mark": self.mark,
            "grade": self.grade,
        }