import tkinter as tk
from tkinter import messagebox 

from gui.change_password_gui import ChangePasswordGUI
from cli.subject_enrolment import add_subject, delete_subject

class SubjectEnrolmentGUI:
    def __init__(self, root, app, student):
        self.root = root
        self.app = app
        self.student = student

    def enrolment_window(self):
        self.enrol_title = tk.Label (
            self.root,
            text = "This is Subject Enrolment System",
            **self.app.title_style
        )
        self.enrol_title.pack(
            pady = self.app.title_padding
        )

        self.enrol_sub_title = tk.Label(
            self.root,
            text = f"Welcome, {self.student.name} ({self.student.student_id}) Please choose a following option",
            **self.app.sub_title_style
        )
        self.enrol_sub_title.pack(
            pady=self.app.sub_title_padding
        )

#enrolment system label 
        panel = self.app.create_menu_panel()
        self.enrol_subject_button = self.app.create_menu_button(panel, "Enrol in a subject", self.enrol_subject)
        self.view_enrolment_button = self.app.create_menu_button(panel,"view enrolment", self.view_enrolment)
        self.remove_subject_button = self.app.create_menu_button(panel,"Remove a subject",self.remove_subject)
        self.change_password_button = self.app.create_menu_button(panel, "Change the Password", self.change_password)
        self.logout_button = self.app.create_menu_button(panel, "Logout", self.logout, is_back=True)


    def change_password(self):
        self.app.clear_window()

        change_password = ChangePasswordGUI(
            self.root, 
            self.app,
            self.student
        )
        change_password.change_password_window()

    def not_implemented(self):
        messagebox.showinfo(
            "Not Implemented",
            "This functionality has not been implemented yet."
        )

    def logout(self):
        self.app.current_student = None
        self.app.login_page()

    def back_to_enrolment(self):
        self.app.subject_enrolment_page(self.student)

    # enrol: no extra page, just show the result in a message box
    def enrol_subject(self):
        subject = add_subject(
            self.student, 
            self.app.students, 
            self.app.database
        )

        if subject is None:
            messagebox.showerror(
                "Enrolment Limit",
                "Students are allowed to enrol in 4 subjects only."
            )
            return

        messagebox.showinfo(
            "Enrolment Successful",
            f"Enrolled in Subject-{subject.subject_id}\n"
            f"You are now enrolled in {len(self.student.subjects)} out of 4 subjects."
        )

    # list of enrolled subjects (used by view and remove pages)
    def show_subject_list(self):
        if not self.student.subjects:
            tk.Label(
                self.root,
                text="No subjects enrolled yet.",
                **self.app.form_label_style
            ).pack(pady=5)
            return

        for subject in self.student.subjects:
            tk.Label(
                self.root,
                text=f"Subject-{subject['id']}  |  Mark: {subject['mark']}  |  Grade: {subject['grade']}",
                **self.app.form_label_style
            ).pack(pady=3)

    # view enrolment page
    def view_enrolment(self):
        self.app.clear_window()

        tk.Label(
            self.root,
            text=f"Enrolled Subjects ({len(self.student.subjects)}/4)",
            **self.app.title_style
        ).pack(pady=self.app.title_padding)

        self.show_subject_list()

        self.app.create_form_button(self.root, "Back", self.back_to_enrolment, is_back=True)

    # remove subject page
    def remove_subject(self):
        self.app.clear_window()

        tk.Label(
            self.root,
            text="Remove a Subject",
            **self.app.title_style
        ).pack(pady=self.app.title_padding)

        self.show_subject_list()

        tk.Label(
            self.root,
            text="Subject ID",
            **self.app.form_label_style
        ).pack(pady=(15, 5))

        self.subject_id_entry = tk.Entry(
            self.root,
            **self.app.form_entry_style
        )
        self.subject_id_entry.pack(pady=(0, 10))

        self.app.create_form_button(self.root, "Remove", self.confirm_remove)
        self.app.create_form_button(self.root, "Back", self.back_to_enrolment, is_back=True)

    def confirm_remove(self):
        subject_id = self.subject_id_entry.get().strip()

        if delete_subject(self.student, self.app.students, self.app.database, subject_id):
            messagebox.showinfo(
                "Subject Removed",
                f"Subject-{subject_id} has been removed."
            )
            self.remove_subject()  # refresh the page with the updated list
        else:
            messagebox.showerror(
                "Remove Failed",
                f"Subject-{subject_id} is not in your enrolment list."
            )