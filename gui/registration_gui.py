#student registration page, entering, name, email, and password 
# student class and database. 

#validateEMail (): input없음=> GUI 그대로 사용 
#registerStudent(): input으로 학생정보를 받아야함, GUI 버튼에 직접 연결하고 터미널 입력 기다리기 => thinter entry로 학생정보 입력받기 

import tkinter as tk
from tkinter import messagebox

class registrationGUI:
    def __init__(self, root, app): #backcommand-  exit or back 버튼을 누를때, 부모창인 app_main_gui.py이 뒤로가기 버튼 누르면 실행할 함수를 전달하는거
        self.root = root
        self.app = app #받아온 객체를 registrationGUI 자신의 속성으로 저장

    def window(self):
        #registration title
        self.regiTitle = tk.Label(
        self.root,
        text="This is Student Registration Page",
        **self.app.titleStyle
    )
        self.regiTitle.pack (
            pady=self.app.titlePadding
            )

        #registrations subTitle 
        self.regiSubTitle = tk.Label(
            self.root,
            text = "please enter you details below to create an account",
            font = self.app.subTitleFont,
            bg=self.app.bgColor,
            fg=self.app.subTextColor
        )
        self.regiSubTitle.pack(
            pady=self.app.subTitlePadding
            )
        
#student NAme label
        self.nameLabel = tk.Label(
            self.root,
            text = "Full Name",
            **self.app.formLabelStyle
        )
        self.nameLabel.pack(pady=(5,5))
#sutdent Name enter box
        self.nameEntry =tk.Entry( #tk.label: 입력항목-보여주는거, tk.Entry: 실체 사용자 입력공간
            self.root,
            **self.app.formEntryStyle
        )
        self.nameEntry.pack(pady=(0,10))


# Student Email Label
        self.emailLabel = tk.Label(
            self.root,
            text="University Email",
            **self.app.formLabelStyle
        )
        self.emailLabel.pack(pady=(5, 5))
# Student Email Entry
        self.emailEntry = tk.Entry(
            self.root,
            **self.app.formEntryStyle
        )
        self.emailEntry.pack(pady=(0, 10))


# Student Password Label
        self.passwordLabel = tk.Label(
            self.root,
            text="Password",
            **self.app.formLabelStyle
        )
        self.passwordLabel.pack(pady=(5, 5))
#student Enter form 
# Password Entry
        self.passwordEntry = tk.Entry(
            self.root,
            **self.app.formEntryStyle,
            show="*"
        )
        self.passwordEntry.pack(pady=(0, 10))

#button
#registration confirmation button => link to the registration 
        self.confirmButton = self.app.createFormButton(
            self.root,
            "Confirm",
            self.registerStudent
        )
        self.exitButton = self.app.createFormButton(
            self.root,
            "Back to Student Menu",
            self.app.studentMenu,
            isBack=True
        )


    def registerStudent(self):
        # Get student information from Entry widgets
        name = self.nameEntry.get().strip()
        email = self.emailEntry.get().strip()
        password = self.passwordEntry.get()

        # Check empty fields
        if not name or not email or not password:
            messagebox.showerror(
                "Registration Failed",
                "Please fill in all required fields."
            )
            return

        messagebox.showinfo(
            "Registration Test",
            f"Name: {name}\nEmail: {email}\nInformation received!"
        )