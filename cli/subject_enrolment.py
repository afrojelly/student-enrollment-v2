import random

from cli.change_password import changePassword
from cli.subject import Subject

MAX_SUBJECTS = 4


def subjectEnrolmentSystem(student, students, database):
    while True:
        print(f"\nWelcome to the Subject Enrolment System , {student.name}. Please choose a following option: ")
        print ("(c) change password")
        print( "(e) enrol in a subject")
        print ("(r) remove a subject")
        print ("(s) show enrolled subjects")
        print ("(x) exit")
        choice = input("Enter your choice (c-e-r-s-x): ").lower()

        if choice == 'c':
            changePassword(student, students, database)

        elif choice == 'e':
            enrolSubject(student, students, database)

        elif choice == 'r':
            removeSubject(student, students, database)

        elif choice == 's':
            viewEnrolment(student)

        elif choice == 'x':
            print("Exiting the Subject Enrolment System.")
            break

        else:
            print("Invalid. Please try again.")


# ---------- logic functions (no input/print -> reused by GUI) ----------

# 301: True if the student can still enrol (less than 4 subjects)
def checkEnrolmentLimit(student):
    return len(student.subjects) < MAX_SUBJECTS


# 302: unique 3-digit subject ID (same idea as generateStudentId)
def generateSubjectId(student):
    existingIds = {subject["id"] for subject in student.subjects}
    while True:
        subjectId = str(random.randint(1, 999)).zfill(3)
        if subjectId not in existingIds:
            return subjectId


# 300: add a new subject and save -> returns the Subject, or None if limit reached
def addSubject(student, students, database):
    if not checkEnrolmentLimit(student):
        return None

    subject = Subject(generateSubjectId(student))
    student.subjects.append(subject.toRecord())
    database.saveStudent(students)
    return subject


# 303: find the subject by ID, remove it and save -> True if removed
def deleteSubject(student, students, database, subjectId):
    for subject in student.subjects:
        if subject["id"] == subjectId:
            student.subjects.remove(subject)
            database.saveStudent(students)
            return True

    return False


# ---------- CLI functions ----------

def enrolSubject(student, students, database):
    subject = addSubject(student, students, database)

    if subject is None:
        print("Students are allowed to enrol in 4 subjects only.")
        return

    print(f"Enrolling in Subject-{subject.subjectId}")
    print(f"You are now enrolled in {len(student.subjects)} out of {MAX_SUBJECTS} subjects.")


def removeSubject(student, students, database):
    subjectId = input("Remove Subject by ID: ").strip()

    if deleteSubject(student, students, database, subjectId):
        print(f"Dropping Subject-{subjectId}")
        print(f"You are now enrolled in {len(student.subjects)} out of {MAX_SUBJECTS} subjects.")
    else:
        print(f"Subject-{subjectId} is not in your enrolment list.")


# 304: show the current enrolment list
def viewEnrolment(student):
    print(f"Showing {len(student.subjects)} subjects")

    if not student.subjects:
        print("No subjects enrolled yet.")
        return

    for subject in student.subjects:
        print(f"[ Subject::{subject['id']} -- mark = {subject['mark']} -- grade = {subject['grade']} ]")