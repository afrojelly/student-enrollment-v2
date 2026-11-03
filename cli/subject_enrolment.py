import random
 
from cli.change_password import change_password
from cli.subject import Subject
 
MAX_SUBJECTS = 4
 
def subject_enrolment_system(student, students, database):
    while True:
        print(f"\nWelcome to the Subject Enrolment System , {student.name}. Please choose a following option: ")
        print( "(e) enrol in a subject")
        print ("(s) show enrolled subjects")
        print ("(r) remove a subject")
        print ("(c) change password")
        print ("(x) exit")
        choice = input("Enter your choice (c-e-r-s-x): ").lower()
 
        if choice == 'e':
            enrol_subject(student, students, database)

        elif choice == 's':
            view_enrolment(student)

        elif choice == 'r':
            remove_subject(student, students, database)

        elif choice == 'c':
            change_password(student, students, database)

        elif choice == 'x':
            print("Exiting the Subject Enrolment System.")
            break

        else:
            print("Invalid. Please try again.")
 
# logic functions

# Max subject check
def check_enrolment_limit(student):
    return len(student.subjects) < MAX_SUBJECTS
 
# add a new subject and save
def add_subject(student, students, database):
    if not check_enrolment_limit(student):
        return None
 
    subject = Subject(student)
    student.subjects.append(subject.to_record())
    database.save_student(students)
    return subject
 
# delete subject, remove it and save
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