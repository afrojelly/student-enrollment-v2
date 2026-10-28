import re

def isValidStudentId(studentId):
    return re.fullmatch(r"[0-9]{6}", studentId) is not None