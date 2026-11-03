import random

from cli.change_password import change_password
from cli.subject import Subject

MAX_SUBJECTS = 4

def subject_enrolment_system(student, students, database):
    while True:
        print(f"\nWelcome to the Subject Enrolment System , {student.name}. Please choose a following option: ")
        print ("(c) change password")
        print( "(e) enrol in a subject")
        print ("(r) remove a subject")
        print ("(s) show enrolled subjects")
        print ("(x) exit")
        choice = input("Enter your choice (c-e-r-s-x): ").lower()

        if choice == 'c':
            change_password(student, students, database)

        elif choice == 'e':
            enrol_subject(student, students, database)

        elif choice == 'r':
            remove_subject(student, students, database)

        elif choice == 's':
            view_enrolment(student)

        elif choice == 'x':
            print("Exiting the Subject Enrolment System.")
            break

        else:
            print("Invalid. Please try again.")


# logic functions

# 301: True if the student can still enrol (less than 4 subjects), 과목 등록 체크 함수
def check_enrolment_limit(student):
    return len(student.subjects) < MAX_SUBJECTS


# 302: unique 3-digit subject ID, Subject ID 생성 함수
def generate_subject_id(student):
    existing_ids = {subject["id"] for subject in student.subjects}
    while True:
        subject_id = str(random.randint(1, 999)).zfill(3)
        if subject_id not in existing_ids:
            return subject_id


# 300: add a new subject and save -> returns the Subject, or None if limit reached
def add_subject(student, students, database):
    if not check_enrolment_limit(student):
        return None

    subject = Subject(generate_subject_id(student))
    student.subjects.append(subject.to_record())
    database.save_student(students)
    return subject


# 303: find the subject by ID, remove it and save -> True if removed
def delete_subject(student, students, database, subject_id):
    for subject in student.subjects:
        if subject["id"] == subject_id:
            student.subjects.remove(subject)
            database.save_student(students)
            return True

    return False


# CLI

def enrol_subject(student, students, database):
    subject = add_subject(student, students, database)

    if subject is None:
        print("Students are allowed to enrol in 4 subjects only.")
        return

    print(f"Enrolling in Subject-{subject.subject_id}")
    print(f"You are now enrolled in {len(student.subjects)} out of {MAX_SUBJECTS} subjects.")


def remove_subject(student, students, database):
    subject_id = input("Remove Subject by ID: ").strip()

    if delete_subject(student, students, database, subject_id):
        print(f"Dropping Subject-{subject_id}")
        print(f"You are now enrolled in {len(student.subjects)} out of {MAX_SUBJECTS} subjects.")
    else:
        print(f"Subject-{subject_id} is not in your enrolment list.")


# View enrolment 함수
def view_enrolment(student):
    print(f"Showing {len(student.subjects)} subjects")

    if not student.subjects:
        print("No subjects enrolled yet.")
        return

    for subject in student.subjects:
        print(f"[ Subject::{subject['id']} -- mark = {subject['mark']} -- grade = {subject['grade']} ]")