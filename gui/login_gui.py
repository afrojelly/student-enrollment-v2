#emain and password enter page 

from cli.login import validateLogin 

from cli.student import Student 

import tkinter as tk
from tkinter import messagebox 


class loginGUI:
    def __init__(self, root, app):
        self.root=root
        self.app=app #app에서 받아온 객체를 loginGUI에서 자기 속성으로 저장 

    def clearPlaceholder(self, event, entry, placeholder, isPassword=False):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg=self.app.bgColor)

            if isPassword:
                entry.config(show="*")


    def showPlaceholder(self, event, entry, placeholder, isPassword=False):
        if entry.get() == "":
            if isPassword:
                entry.config(show="")

            entry.insert(0, placeholder)
            entry.config(fg="grey")


    def loginWindow(self):
        self.loginTitle = tk.Label(
            self.root,
            text ="This is student Login Page",
            **self.app.titleStyle
    )
        self.loginTitle.pack (
            pady=self.app.titlePadding
            )

        self.loginSubTitle = tk.Label(
            self.root,
            text = "please login with your validated email and password",
            **self.app.subTitleStyle
        )
        self.loginSubTitle.pack(
            pady=self.app.subTitlePadding
            )

        
# Email Label
        self.emailLabel = tk.Label(
            self.root,
            text="University Email",
            **self.app.formLabelStyle
        )
        self.emailLabel.pack(pady=(5, 5))

# Email Entry
        self.emailEntry = tk.Entry(
            self.root,
            **self.app.formEntryStyle
        #이 상자 안에 hint를 넣고, user가 입력을 사작하면 clear 하고 입력값을 받을 수 는 없나? 
        )
        self.emailEntry.pack(pady=(0, 10))

 # form box placeholder 

        self.emailPlaceholder = "firstname.lastname@university.com"

        self.emailEntry.insert (0, self.emailPlaceholder)
        self.emailEntry.config (fg ="grey")       
#(tkinter) bind() =>method : 특정 이벤트(Event)(e.g.: 마우스 클릭, 키보드 입력, Focus 이동 등)이 윈도우에서 발생했을 때 실행할 Callback Function
        self.emailEntry.bind(
            "<FocusIn>",
            lambda event: self.clearPlaceholder(
                event,
                self.emailEntry,
                self.emailPlaceholder
            )
        )

        # When leaving the Entry
        self.emailEntry.bind(
            "<FocusOut>",
            lambda event: self.showPlaceholder(
                event,
                self.emailEntry,
                self.emailPlaceholder
            )
        )

#Password
        self.passwordLabel=tk.Label(
            self.root,
            text="Password",
            **self.app.formLabelStyle
        )
        self.passwordLabel.pack(pady=(5,5))

        self.passwordEntry = tk.Entry(
            self.root, 
            **self.app.formEntryStyle
        )
        self.passwordEntry.pack (pady =(0,10))

        self.passwordPlaceholder = "Enter your password"
        self.passwordEntry.insert (0,self.passwordPlaceholder)
        self.passwordEntry.config(fg="grey", show="")

        # When clicking inside the Entry
        self.passwordEntry.bind(
            "<FocusIn>",
            lambda event: self.clearPlaceholder(
                event,
                self.passwordEntry,
                self.passwordPlaceholder,
                isPassword=True
            )
        )

        # When leaving the Entry
        self.passwordEntry.bind(
            "<FocusOut>",
            lambda event: self.showPlaceholder(
                event,
                self.passwordEntry,
                self.passwordPlaceholder,
                isPassword=True
            )
        )

        # Connect Subject Enrolment GUI here when ready

        self.loginButton = self.app.createFormButton(
            self.root,
            "Login",
            self.loginStudent
        )

        self.exitButton = self.app.createFormButton(
            self.root,
            "Back to Student Menu",
            self.app.studentMenu,
            isBack=True
        )

    def loginStudent(self):
        email =self.emailEntry.get().strip()
        password = self.passwordEntry.get()

        if email == self.emailPlaceholder:
            email = ""
        if password == self.passwordPlaceholder:
            password = ""

        if not email or not password:
            messagebox.showerror(
            "Login Failed",
            "Please enter your email and password."
        )
            return
        
        self.app.students = self.app.database.loadStudents()

        # Validate using CLI function
        student = validateLogin(
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
        
        self.app.currentStudent = student
        messagebox.showinfo(
            "Login Successful",
            f"Welcome, {student.name}!\n"
            f"Student ID: {student.studentId}"
        )

        self.app.subjectEnrolmentPage(student) # 실제 로그인한 학생객체
