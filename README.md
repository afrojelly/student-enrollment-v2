# student_enrollment_interface_cmp1-07-group2  
UTS Faculty of Engineering and Information Technology (FEIT)  
Subject: Fundamentals of Software Development  
Assessment: Student Enrolment Interface  
Team: CMP1-07-GROUP2  


## overview
The Student Enrolment Interface is a Python-based application developed as part of the Fundamentals of Software Development assessment at the University of Technology Sydney (UTS). The application provides both a Command-Line Interface (CLI) and a Graphical User Interface (GUI) using Tkinter. 
The system supports student registration, authentication, password management, subject enrolment, and administrative student management through separate menu-based subsystems.
Student information is stored locally in a JSON-formatted data file `students.data`, allowing student records and enrolment information to persist between program sessions.

## How to Run
**Requirement**
- Python 3
- Tkinter for the graphical interface
- A terminal or IDE capable of running Python
- No external Python packages are required for the features described here.


**Python Scripts**
Clone the repository:

1. git clone https://github.com/jisunbella/student-enrollment-interface-cmp1-07-group2.git 
2. Open the project folder:

cd student-enrollment-interface-cmp1-07-group2

**Run the CLI**

from the project root dirctory:

```bash
python python -m cli.uni_app_main
```

Follow the terminal menu instructions.

**Runt the GUI**

from the project root dirctory: 

```bash
python python -m gui.app_main_gui
```

The GUI should open a Tkinter window where users can access the application's features.


***Important Import Instructions***

Since the project separates CLI and GUI into different folders, both applications should be run using Python's module execution option (-m).

For example:

from cli.student import Student   
from cli.database import Database

Running python cli/uni_app_main.py directly may cause ModuleNotFoundError when package imports are used.


## Project Features 
The project scope includes:
- **Student registration:** Create an account with a name, university email address, and password.
- **Student login:** Verify login credentials against saved student records.
- **Password management:** Allow logged-in students to change their password.
- **Subject enrolment:** Enrol in subjects (Max 4), remove subjects, and view enrolled subjects.
- **Administration:** Provide a separate menu for administrative functions.

## Student System_Registration Rules and Error Handling
### Email Validation   
Email addresses must follow this format:

'firstname.lastname@university.com'

Requirements:
- The email must contain a first name and last name separated by exactly one dot.
- The first and last name sections must contain English letters only.
- The email must end with @university.com.
- The email must be unique within the student database.

Examples
|**Email**                | **Result**| **reason**       |
|-------------------------|-----------|------------------|  
|robyn.you@university.com | valid     |correct format    |
|Jisunlee@university.com  | invalid   | Missing separator| 
|HJ.Han@gmail.com         | Invalid   | incorrect domain | 
|Existing registered email| Invalid   | Duplicate email  |


If any of these requirements are not satisfied, registration must be rejected and an appropriate error message displayed.

### Password Validation 

Student passwords must satisfy all the following requirements:

- Start with an uppercase English letter.
- Contain at least five English letters, including the first letter.
- Contain at least three digits.
- Contain only English letters and digits.
- Letters and digits may appear in any order after the first character.

Students may use the same password as other students, provided that the password satisfies the validation requirements.

An invalid password must be rejected, with an error message explaining the required format.

### Student ID Geeneration

Each successfully registered student receives a unique, randomly generated student ID.

Rules:
- Generated between 1 and 999,999.
- Formatted as a six-digit string.
- Leading zeros are added when necessary.
- IDs must not duplicate existing student IDs.

Example: `123456`.

After successful registration, the new student record is saved to the database.


## Student System_Login and Password Management 
### Student Login 

A registered student can log in using their university email address and password.

The system:
- Reads registered student records from the database.
- Checks whether the email address exists.
- Verifies the supplied password.
- Displays an error message if authentication fails.
- Opens the Subject Enrolment System after successful authentication.

### Change Password 

Logged-in students can change their passwords through the Subject Enrolment System.

The process includes:
-  Entering the current password.
- Verifying the current password against the stored record.
- Entering a new password.
- Validating the new password using the registration password rules.
- Confirming the new password.
- Saving the updated password to the database.

The system rejects an incorrect current password, an invalid new password, or a password confirmation mismatch.

The password rule is same as registration process. 

## student entroment rule and error 

#need to fixed
#max number 4
#Subject ID and score generation 
#subject remove 
#showing error 


## Admin rule and error 

#shows grade = average of 4 subject and ~~
#error rule 




## System Menus

### University System

|**Option**| **Action**              |  
|----------|-------------------------|  
| A        | Open the Admin System   |  
| S        | Open the Student System |  
| X        | Exit the application    |  

### Student System

student can choose Register, if has not registered, and can start the login with the registered Email and Password

|**Option**| **Action**                      |  
|----------|---------------------------------|  
| l        | Log in                          |  
| r        | Register                        |  
| x        | Return to the University System |  

### Subject Enrolment System

This menu is accessed after a successful login.

|**Option**| **Action**                        |  
|----------|-----------------------------------|  
| c        | Change password                   |  
| e        | Enrol in a subject                |  
| r        | Remove a subject                  |  
| s        | Show enrolled subjects            |  
| x        | Exit the Subject Enrolment System |  

### Admin System

Admin does not need to register for accessing the systen. 

|**Option**| **Action**                        |  
|----------|-----------------------------------|
| V        | view all student                  |  
| O        | Organise student by grade         |  
| C        | Categorise students P/F           |  
| R        | Remove student By ID (individual) |  
| L        | clear student data (entire)       |  
| X        | Exit the Admin Systme             |  


## Data Storage

Each student record contains:
- Name
- Email address
- Password
- Student ID
- Enrolled subjects (0-4)

This Database class provides the following mehods: 
- `saveStudent(studentsInfo)`: Saves the student list to `students.data`.
- `loadStudents()`: Reads saved records and recreates Student objects.

IF the data file does not exist, the application creates it automatically in the file 

## CLI and GUI 

- CLI: terminal base student enrolment system 
- GUI: Tkinter grapich interface 

student-enrollment-interface-cmp1-07-group2/  
│  
├── cli/  
│   ├── admin.py  
│   ├── change_password.py  
│   ├── database.py  
│   ├── login.py  
│   ├── registration.py  
│   ├── student.py  
│   ├── students.data  
│   ├── subject_enrolment.py  
│   ├── subject.py  
│   ├── uni_app_main.py  
│   └── uni_system.py  
│  
├── gui/  
│   ├── __init__.py    
│   ├── app_main_gui.py  
│   ├── registration_gui.py  
│   ├── login_gui.py  
│   ├── change_password_gui.py  
│   └── subject_gui.py  
│  
├── .gitignore  
└── README.md  


## Team

**Team:** cmp1-07-group2

This application is developed collaboratively, with team members contributing to individual features and system integration.

- Hyejin Han (26510228): Subject_Enrolment 
- Jisun Lee (26645135): Admin_system 
- Robyn You (25960535): uni_System & Student_system 
- Ryeongeun Kim (26639361): Subject_Enrolment 







#README. file: imformation of project 

#all the detail need to be in the readme.

#contribuition => which feature who import ///

#example question How the GUI comminicate with the GUI 

     #CLI/GUI/Report file 
