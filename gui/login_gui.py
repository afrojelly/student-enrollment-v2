#emain and password enter page 

from cli.student_login import validate_login

from cli.student import Student 

import tkinter as tk
from tkinter import messagebox 


class LoginGUI:
    def __init__(self, root, app):
        self.root=root
        self.app=app # Store the app object on this LoginGUI instance.

    def clear_placeholder(self, event, entry, placeholder, is_password=False):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg=self.app.bg_color)

            if is_password:
                entry.config(show="*")


    def show_placeholder(self, event, entry, placeholder, is_password=False):
        if entry.get() == "":
            if is_password:
                entry.config(show="")

            entry.insert(0, placeholder)
            entry.config(fg="grey")


    def login_window(self):
        self.login_title = tk.Label(
            self.root,
            text ="This is student Login Page",
            **self.app.title_style
    )
        self.login_title.pack (
            pady=self.app.title_padding
            )

        self.login_sub_title = tk.Label(
            self.root,
            text = "please login with your validated email and password",
            **self.app.sub_title_style
        )
        self.login_sub_title.pack(
            pady=self.app.sub_title_padding
            )

        
# Email Label
        self.email_label = tk.Label(
            self.root,
            text="University Email",
            **self.app.form_label_style
        )
        self.email_label.pack(pady=(5, 5))

# Email Entry
        self.email_entry = tk.Entry(
            self.root,
            **self.app.form_entry_style
        #이 상자 안에 hint를 넣고, user가 입력을 사작하면 clear 하고 입력값을 받을 수 는 없나? 
        )
        self.email_entry.pack(pady=(0, 10))

 # form box placeholder 

        self.email_placeholder = "firstname.lastname@university.com"

        self.email_entry.insert (0, self.email_placeholder)
        self.email_entry.config (fg ="grey")
#(tkinter) bind() =>method : 특정 이벤트(Event)(e.g.: 마우스 클릭, 키보드 입력, Focus 이동 등)이 윈도우에서 발생했을 때 실행할 Callback Function
        self.email_entry.bind(
            "<FocusIn>",
            lambda event: self.clear_placeholder(
                event,
                self.email_entry,
                self.email_placeholder
            )
        )

        # When leaving the Entry
        self.email_entry.bind(
            "<FocusOut>",
            lambda event: self.show_placeholder(
                event,
                self.email_entry,
                self.email_placeholder
            )
        )

#Password
        self.password_label=tk.Label(
            self.root,
            text="Password",
            **self.app.form_label_style
        )
        self.password_label.pack(pady=(5,5))

        self.password_entry = tk.Entry(
            self.root, 
            **self.app.form_entry_style
        )
        self.password_entry.pack (pady =(0,10))

        self.password_placeholder = "Enter your password"
        self.password_entry.insert (0,self.password_placeholder)
        self.password_entry.config(fg="grey", show="")

        # When clicking inside the Entry
        self.password_entry.bind(
            "<FocusIn>",
            lambda event: self.clear_placeholder(
                event,
                self.password_entry,
                self.password_placeholder,
                is_password=True
            )
        )

        # When leaving the Entry
        self.password_entry.bind(
            "<FocusOut>",
            lambda event: self.show_placeholder(
                event,
                self.password_entry,
                self.password_placeholder,
                is_password=True
            )
        )

        # Connect Subject Enrolment GUI here when ready

        self.login_button = self.app.create_form_button(
            self.root,
            "Login",
            self.login_student
        )

        self.exit_button = self.app.create_form_button(
            self.root,
            "Back to Student Menu",
            self.app.student_menu,
            is_back=True
        )

    def login_student(self):
        email =self.email_entry.get().strip()
        password = self.password_entry.get()

        if email == self.email_placeholder:
            email = ""
        if password == self.password_placeholder:
            password = ""

        if not email or not password:
            messagebox.showerror(
            "Login Failed",
            "Please enter your email and password."
        )
            return
        
        self.app.students = self.app.database.load_students()

        # Validate using CLI function
        student = validate_login(
            self.app.students,
            email,
            password
        )

        if student is None:
            messagebox.showerror(
                "Login Failed",
                "Incorrect email or password."
            )
            return
        
        self.app.current_student = student
        messagebox.showinfo(
            "Login Successful",
            f"Welcome, {student.name}!\n"
            f"Student ID: {student.student_id}"
        )

        self.app.current_student=student #로그인한 객체 저장
        self.app.subject_enrolment_page(student) # 학생개체 페이지 호출
