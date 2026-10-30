import tkinter as tk
from tkinter import messagebox 

from gui.change_password_gui import changePasswordGUI
from cli.subject_enrolment import addSubject, deleteSubject

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
        self.enrolSubjectButton = self.app.createMenuButton(panel, "Enrol in a subject", self.enrolSubject)
        self.removeSubjectButton = self.app.createMenuButton(panel,"Remove a subject",self.removeSubject)
        self.viewEnrolmentButton = self.app.createMenuButton(panel,"view enrolment", self.viewEnrolment)
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

    def backToEnrolment(self):
        self.app.subjectEnrolmentPage(self.student)

    # enrol: no extra page, just show the result in a message box
    def enrolSubject(self):
        subject = addSubject(self.student, self.app.students, self.app.database)

        if subject is None:
            messagebox.showerror(
                "Enrolment Limit",
                "Students are allowed to enrol in 4 subjects only."
            )
            return

        messagebox.showinfo(
            "Enrolment Successful",
            f"Enrolled in Subject-{subject.subjectId}\n"
            f"You are now enrolled in {len(self.student.subjects)} out of 4 subjects."
        )

    # list of enrolled subjects (used by view and remove pages)
    def showSubjectList(self):
        if not self.student.subjects:
            tk.Label(
                self.root,
                text="No subjects enrolled yet.",
                **self.app.formLabelStyle
            ).pack(pady=5)
            return

        for subject in self.student.subjects:
            tk.Label(
                self.root,
                text=f"Subject-{subject['id']}  |  Mark: {subject['mark']}  |  Grade: {subject['grade']}",
                **self.app.formLabelStyle
            ).pack(pady=3)

    # view enrolment page
    def viewEnrolment(self):
        self.app.clearWindow()

        tk.Label(
            self.root,
            text=f"Enrolled Subjects ({len(self.student.subjects)}/4)",
            **self.app.titleStyle
        ).pack(pady=self.app.titlePadding)

        self.showSubjectList()

        self.app.createFormButton(self.root, "Back", self.backToEnrolment, isBack=True)

    # remove subject page
    def removeSubject(self):
        self.app.clearWindow()

        tk.Label(
            self.root,
            text="Remove a Subject",
            **self.app.titleStyle
        ).pack(pady=self.app.titlePadding)

        self.showSubjectList()

        tk.Label(
            self.root,
            text="Subject ID",
            **self.app.formLabelStyle
        ).pack(pady=(15, 5))

        self.subjectIdEntry = tk.Entry(
            self.root,
            **self.app.formEntryStyle
        )
        self.subjectIdEntry.pack(pady=(0, 10))

        self.app.createFormButton(self.root, "Remove", self.confirmRemove)
        self.app.createFormButton(self.root, "Back", self.backToEnrolment, isBack=True)

    def confirmRemove(self):
        subjectId = self.subjectIdEntry.get().strip()

        if deleteSubject(self.student, self.app.students, self.app.database, subjectId):
            messagebox.showinfo(
                "Subject Removed",
                f"Subject-{subjectId} has been removed."
            )
            self.removeSubject()  # refresh the page with the updated list
        else:
            messagebox.showerror(
                "Remove Failed",
                f"Subject-{subjectId} is not in your enrolment list."
            )