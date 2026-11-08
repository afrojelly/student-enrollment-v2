from cli.utils import colour, RED, GREEN, YELLOW, CYAN
from cli.change_password import change_password
from cli.subject import Subject

MAX_SUBJECTS = 4

def subject_enrolment_system(student, students, database):
    while True:
        print(colour(f"\nWelcome to the Subject Enrolment, {student.name}. Please choose a following option: ", CYAN))
        print(colour(" \t(c) change password", CYAN))
        print(colour(" \t(e) enrol in a subject", CYAN))
        print(colour(" \t(r) remove a subject", CYAN))
        print(colour(" \t(s) show enrolled subjects", CYAN))
        print(colour(" \t(x) exit", CYAN))
        choice = input(colour(" \t Enter your choice (c-e-r-s-x): ", CYAN)).lower()

        if choice == 'c':
            change_password(student, students, database)
        
        elif choice == 'e':
            enrol_subject(student, students, database)

        elif choice == 'r':
            remove_subject(student, students, database)

        elif choice == 's':
            view_enrolment(student)

        elif choice == 'x':
            print(colour("\tExiting the Subject Enrolment System.", YELLOW))
            break

        else:
            print(colour("\tInvalid. Please try again.", RED))

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
        print(colour("\tStudents are allowed to enrol in 4 subjects only.", RED))
        return

    print(colour(f"\tEnrolling in Subject-{subject.subject_id}", GREEN))
    print(colour(f"\tYou are now enrolled in {len(student.subjects)} out of {MAX_SUBJECTS} subjects.", YELLOW))

def remove_subject(student, students, database):
    subject_id = input("\tRemove Subject by ID: ").strip()

    if delete_subject(student, students, database, subject_id):
        print(colour(f"\tDropping Subject-{subject_id}", YELLOW))
        print(colour(f"\tYou are now enrolled in {len(student.subjects)} out of {MAX_SUBJECTS} subjects.", YELLOW))
    else:
        print(colour(f"\tSubject-{subject_id} is not in your enrolment list.", RED))

# View enrolment 함수
def view_enrolment(student):
    print(colour(f"\tShowing {len(student.subjects)} subjects", YELLOW))

    if not student.subjects:
        print(colour("\tNo subjects enrolled yet.", YELLOW))
        return

    for subject in student.subjects:
        print(f"\t[ Subject::{subject['id']} -- mark = {subject['mark']} -- grade = {subject['grade']} ]")