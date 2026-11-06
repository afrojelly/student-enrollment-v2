import re

# Utility functions for validation
def is_valid_student_id(student_id):
    pattern = r"^[0-9]{6}$"
    return re.fullmatch(pattern, student_id) is not None

def validate_email(email):
    pattern = r"[A-Za-z]+\.[A-Za-z]+@university\.com"
    return bool(re.fullmatch(pattern, email))

def validate_password(password):
    pattern = r"[A-Z][A-Za-z]{4,}[0-9]{3,}"
    return bool(re.fullmatch(pattern, password))

# Utility functions for grading
def get_grade(mark):
    if mark >= 85:
        return "HD"
    if mark >= 75:
        return "D"
    if mark >= 65:
        return "C"
    if mark >= 50:
        return "P"
    return "Z"

# Utility function to go back to the previous menu
def go_back(value = None):
    print("Returning to the previous menu.")
    return value