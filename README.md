# student_enrollment_interface_cmp1-07-group2
Developed for UTS FEIT, Fundamental of Software Development, Assessment 
by team **CMP1-07-GROUP3**

## overview
CLIUniApp is a Python command-line application developed as part of the Fundamentals of Software Development subject. It is designed to support student self-enrolment and administrative student management through separate, menu-based subsystems.
The Student System provides registration and login, followed by access to password management and subject enrolment services. The Admin System is designed to allow administrators to manage student records.
Student records are stored locally in `students.data` using JSON format, preserving student details and enrolment information between program sessions.

## Project Features 
The project scope includes:
- **Student registration:** Create an account with a name, university email address, and password.
- **Student login:** Verify login credentials against saved student records.
- **Password management:** Allow logged-in students to change their password.
- **Subject enrolment:** Enrol in subjects (Max 4), remove subjects, and view enrolled subjects.
- **Administration:** Provide a separate menu for administrative functions.

## Registration Validation Rules and error 
### Email Address
Email addresses must follow this format:

'firstname.lastname@university.com'

, where shows erreor if:
- Not matched with the format

     The first and last name sections must contatin English letters only, separtated one dot.  
- have a same Email already exist 

### Password

Passwords must:

- Start with an uppercase English letter.
- Contain at least five English letters, including the first letter.
- Contain at least three digits.
- Contain only English letters and digits.
- Letters and digits may appear in any order after the first character.

Password can be vary among student, while it is acceptable to have the same password with others, while it shows error where one or more password rule isn't matched

### Student ID

Each student is assigned a unique, randomly generated ID between 1 and 999,999.

IDs are displayed as six-digit strings, including leading zeros where necessary. For example: `123456`.


## student entroment rule and error 

#need to fixed
#max number 4
#Subject ID and score generation 
#subject remove 
#showing error 


## Admin rule and error 

#shows grade = average of 4 subject and ~~
#error rule 


## How to Run
**Requirement**

     - python
     - A terminal or an IDE capable of running python\

**Python Scripts**

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the following command:
```bash
python uni_app_main.py
```
4. Follow the menu prompts to register or log in.

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
