#student registration page, entering, name, email, and password 
# student class and database. 

# Validation functions do not require GUI input, so they can be reused directly.
# Registration reads student details from Tkinter entry fields.
from cli.student_registration import (
    validate_email,
    validate_password,
    generate_student_id
)
from cli.student import Student 


import tkinter as tk
from tkinter import messagebox


class RegistrationGUI:
    def __init__(self, root, app): #backcommand-  exit or back 버튼을 누를때, 부모창인 app_main_gui.py이 뒤로가기 버튼 누르면 실행할 함수를 전달하는거
        self.root = root
        self.app = app # Store the app object on this RegistrationGUI instance.

    def regi_window(self):
        #registration title
        self.regi_title = tk.Label(
        self.root,
        text="This is Student Registration Page",
        **self.app.title_style
    )
        self.regi_title.pack (
            pady=self.app.title_padding
            )

        # Registration subtitle.
        self.regi_sub_title = tk.Label(
            self.root,
            text = "please enter you details below to create an account",
            **self.app.sub_title_style
        )
        self.regi_sub_title.pack(
            pady=self.app.sub_title_padding
            )
        
#student NAme label
        self.name_label = tk.Label(
            self.root,
            text = "Full Name",
            **self.app.form_label_style
        )
        self.name_label.pack(pady=(5,5))
#sutdent Name enter box
        self.name_entry =tk.Entry( #tk.label: 입력항목-보여주는거, tk.Entry: 실체 사용자 입력공간
            self.root,
            **self.app.form_entry_style
        )
        self.name_entry.pack(pady=(0,10))


# Student Email Label
        self.email_label = tk.Label(
            self.root,
            text="University Email",
            **self.app.form_label_style
        )
        self.email_label.pack(pady=(5, 5))
# Student Email Entry
        self.email_entry = tk.Entry(
            self.root,
            **self.app.form_entry_style
        )
        self.email_entry.pack(pady=(0, 5))
#Email format hint 
        self.email_hint = tk.Label(
            self.root,
            text = "Format: firstname.lastname@university.com",
            **self.app.hint_style
        )
        self.email_hint.pack(pady=(0,5))

# Student Password Label
        self.password_label = tk.Label(
            self.root,
            text="Password",
            **self.app.form_label_style
        )
        self.password_label.pack(pady=(5, 5))
#student Enter form 
# Password Entry
        self.password_entry = tk.Entry(
            self.root,
            **self.app.form_entry_style,
            show="*"
        )
        self.password_entry.pack(pady=(0, 5))
#Password Hing 
        self.password_hint = tk.Label(
            self.root,
            text = "Must start with uppercase | At least 5 letters | At least 3 digits",
            **self.app.hint_style
        )
        self.password_hint.pack(pady=(0,8))

#button
#registration confirmation button => link to the registration 
        self.confirm_button = self.app.create_form_button(
            self.root,
            "Confirm",
            self.register_student
        )
        self.exit_button = self.app.create_form_button(
            self.root,
            "Back to Student Menu",
            self.app.student_menu,
            is_back=True
        )


    def register_student(self):
        # Get student information from Entry widgets
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get()

        # Check empty fields
        if not name or not email or not password:
            messagebox.showerror(
                "Registration Failed",
                "Please fill in all required fields."
            )
            return
        #validate email format 
        if not validate_email(email):
            messagebox.showerror(
                "Invalid Email",
                "Enter a valid email address:\n"
                "firstname.lastname@university.com"
            )
            return
        #validate Password 
        if not validate_password(password):
            messagebox.showerror(
                "Invalid Password",
                """Please follow the password format.

        Password requirements:
        - Must start with an uppercase letter
        - Contain at least 5 letters
        - Contain at least 3 digits"""
            )
            return

        #load student record 
        # => email duplication check + student Id generation 
        self.app.students = self.app.database.load_students()

        existing_emails ={
            student.email for student in self.app.students
        }
        if email in existing_emails:
            messagebox.showerror(
                "Registration Failed", 
                "This email is already registered."
            )
            return 

        student_id = generate_student_id(self.app.students)

#creating student list and save
        student = Student(name, email, password, student_id)
        new_students = self.app.students +[student]
#data error simulation 
        try:
            self.app.database.save_student(new_students)
        except OSError as error:
            messagebox.showerror(
                "Database Error",
                f"Unable to save student data: {error}"
            )
            return  # 반드시 except 내부!

        # Only executed when saving succeeds
        self.app.students = new_students
        messagebox.showinfo(
            "Registration Successful",
            f"Welcome, {student.name}!\n"
            f"Your Student ID is: {student.student_id}\n\n"
            "Please return to the Student Menu to login."
        )
        self.app.student_menu()


#code recurrunt 
# validate_email(email)
# validate_password(password)
# generate_student_id(students)
#Student 
# Database 