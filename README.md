# student_enrollment_interface_cmp1-07-group2  

UTS Faculty of Engineering and Information Technology (FEIT)  
Subject: Fundamentals of Software Development  
Assessment: Student Enrolment Interface  
Team: CMP1-07-GROUP2

## Overview

The Student Enrolment Interface is a Python application developed for the Fundamentals of Software Development assessment at the University of Technology Sydney (UTS). It provides a command-line interface (CLI) and a graphical user interface (GUI).

Through the CLI, students can register, log in, change their password, and enrol in, view, or remove subjects. 

The CLI also includes an admin system for viewing all students, grouping students by grade, partitioning them into pass/fail, removing a student by ID, and clearing all the student records. 

The GUI is for registered students and provides login and subject-enrolment features.

Student records are stored locally as JSON in `cli/students.data` and persist between runs.

## Requirements

- Python 3
- Tkinter for the GUI
- No third-party Python packages are required

## Running the application

Run commands from the project root directory. Use `python` on Windows or `python3` on macOS/Linux.

### CLI

```bash
python -m cli.uni_app_main
```

### GUI

```bash
python -m gui.app_main_gui
```

The `-m` option runs the applications as modules so their package imports resolve correctly.

## Features and rules

### Student registration and login

- Students can register and log in through the CLI.
- Email addresses must follow `firstname.lastname@university.com`. The first and last name portions must contain English letters and be separated by one dot. Email addresses must be unique.
- Passwords must start with an uppercase English letter, contain more than five English letters in total, and end with at least three digits. Only English letters and digits are allowed. The password may be reused by another student.
- Each new student receives a unique, randomly generated six-digit ID from `000001` to `999999`.
- Registration and login input is validated, and users can cancel supported prompts with `x`.

### Subject enrolment

- A student can enrol in up to four subjects and can remove an enrolled subject.
- Each enrolment receives a randomly generated subject ID from `001` to `999`. IDs are checked against the student's current enrolments.
- Each subject receives a random mark from 25 to 100. Its grade is calculated from that mark:

| Average mark | Grade |
| ------------ | ----- |
| 85 or higher | HD    |
| 75 or higher | D     |
| 65 or higher | C     |
| 50 or higher | P     |
| Below 50     | Z     |

- Enrolment records, including subject IDs, marks, and grades, are saved with the student record.
- The CLI and GUI show an error when the student has reached the four-subject limit.

### Administration (CLI)

The admin menu is available without a separate admin registration or login. Administrators can list all students, group students by their average mark grade, partition students into PASS/FAIL groups, remove a student by ID, or clear all student records.

Grade is determined by the average mark:

| Average mark | Grade |
| ------------ | ----- |
| 85 or higher | HD    |
| 75 or higher | D     |
| 65 or higher | C     |
| 50 or higher | P     |
| Below 50     | Z     |

PASS/FAIL is determined by the average mark:

| Average mark | Result |
| ------------ | ------ |
| 50 or higher | PASS   |
| Below 50     | FAIL   |

## System menus

Menu choices are case-insensitive.

### University System (CLI)

| **Option** | **Action**              |
| ---------- | ----------------------- |
| A          | Open the Admin System   |
| S          | Open the Student System |
| X          | Exit the application    |

### Student System (CLI)

| **Option** | **Action**                      |
| ---------- | ------------------------------- |
| l          | Log in                          |
| r          | Register                        |
| x          | Return to the University System |

### Subject Enrolment System (CLI)

This menu is available after a successful login.

| **Option** | **Action**                      |
| ---------- | ------------------------------- |
| c          | Change password                 |
| e          | Enrol in a subject              |
| r          | Remove a subject                |
| s          | Show enrolled subjects          |
| x          | Return to the Student System    |

### Admin System (CLI)

| **Option** | **Action**                      |
| ---------- | ------------------------------- |
| s          | Show all student                |
| g          | Group students by grade         |
| p          | Partition students to PASS/FAIL |
| r          | Remove a student by ID          |
| c          | clear all the student record    |
| x          | Return to the University System |


## GUI

The GUI is designed for registered students and does not include admin or registration menus. It provides:

- A login page that validates credentials against the saved student records.
- A subject-enrolment menu for enrolling in subjects and changing a password.
- Pages for viewing and removing enrolled subjects.
- Error dialogs for empty login fields, incorrect credentials, invalid email or password fromat, invalid password changes, and attempts to exceed the subject limit.

## Data storage

The `Database` class reads and writes student records in `cli/students.data`. It creates the data file with an empty JSON list if the file does not exist. Student records contain a name, email, password, student ID, and a list of enrolled subjects.

Database operations include:

- `save_student(students_info)`: Save student records.
- `load_students()`: Load records and recreate `Student` objects.
- `get_student(student_id)`: Find a student by ID.
- `delete_student(student_id)`: Remove a student by ID.
- `clear_students()`: Remove all student records while keeping the data file valid.

## Project structure

```text
student-enrollment-v2/
├── cli/
│   ├── admin.py
│   ├── change_password.py
│   ├── database.py
│   ├── student.py
│   ├── student_login.py
│   ├── student_registration.py
│   ├── student_system.py
│   ├── subject.py
│   ├── subject_enrolment.py
│   ├── uni_app_main.py
│   ├── uni_system.py
│   ├── utils.py
│   └── students.data
├── gui/
│   ├── app_main_gui.py
│   ├── change_password_gui.py
│   ├── gui_style.py
│   ├── login_gui.py
│   └── subject_enrolment_gui.py
└── README.md
```

## Team contributions

This application was developed collaboratively, with team members contributing to individual features and system integration.

- Hyejin Han (26510228): Subject enrolment
- Jisun Lee (26645135): Admin system
- Robyn You (25960535): University and student systems
- Ryeongeun Kim (26639361): GUI, Change password 