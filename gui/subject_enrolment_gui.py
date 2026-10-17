import tkinter as tk
from tkinter import messagebox 

from gui.change_password_gui import changePasswordGUI

class subjectEnrolmentGUI:
    def __init__(self, root, app, student):
        self.root = root
        self.app = app
        self.student = student

    def enrolmentWindow(self):
        self.enrolTitle = tk.Label (
            self.root,
            text = "This is Subject Enrolment System",
            **self.app.titleStyle
        )
        self.enrolTitle.pack(
            pady = self.app.titlePadding
        )

        self.enrolSubTitle = tk.Label(
            self.root,
            text = f"Welcome, {self.student.name} ({self.student.studentId}) Please choose a following option",
            **self.app.subTitleStyle
        )
        self.enrolSubTitle.pack(
            pady=self.app.subTitlePadding
        )

#enrolment system label 
        panel = self.app.createMenuPanel()
        self.changePasswordButton = self.app.createMenuButton(panel, "Change the Password", self.changePassword)
        self.enrolSubjectButton = self.app.createMenuButton(panel, "Enrol in a subject", self.notImplemented) #enrolSubject)  # 아직 yet implanted, attibue
        self.removeSubjectButton = self.app.createMenuButton(panel,"Remove a subject",self.notImplemented) #removeSubject) # 
        self.viewEnrolmentButton = self.app.createMenuButton(panel,"view enrolment", self.notImplemented) #vewEnrolment) # 
        self.logoutButton = self.app.createMenuButton(panel, "logout", self.app.mainMenu, self.logout )



    def changePassword(self):
        self.app.clearWindow()

        changePassword = changePasswordGUI(
            self.root, 
            self.app,
            self.student
        )
        changePassword.changePasswordWindow()

    def notImplemented(self):
        messagebox.showinfo(
            "Not Implemented",
            "This functionality has not been implemented yet."
        )

    def logout(self):
        self.app.currentStudent = None
        self.app.studentMenu()