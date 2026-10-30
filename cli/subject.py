import random

class Subject:
    def __init__(self, subjectId):
        self.subjectId = subjectId
        self.mark = self.generateMark()      # 305: mark generated automatically
        self.grade = self.calculateGrade()   # 306: grade calculated from the mark

    # random mark between 25 and 100
    def generateMark(self):
        return random.randint(25, 100)

    # same grading rule as admin.py getGrade()
    def calculateGrade(self):
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
    def toRecord(self):
        return {
            "id": self.subjectId,
            "mark": self.mark,
            "grade": self.grade,
        }