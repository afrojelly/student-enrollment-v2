import random

class Subject:
    def __init__(self, subject_id):
        self.subject_id = subject_id
        self.mark = self.generate_mark()      # 305: mark generated automatically
        self.grade = self.calculate_grade()   # 306: grade calculated from the mark

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