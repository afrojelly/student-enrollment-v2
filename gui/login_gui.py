import tkinter as tk
from tkinter import messagebox

from cli.student_login import find_student_by_credentials
from cli.utils import validate_email, validate_password

# Email and password entry page.
class LoginGUI:
    def __init__(self, root, app):
        self.root = root
        self.app = app  # Store the app object on this LoginGUI instance.

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
            text="Student Login",
            **self.app.title_style
        )
        self.login_title.pack(pady=self.app.title_padding)

        self.login_sub_title = tk.Label(
            self.root,
            text="Please log in with your university email and password.",
            **self.app.sub_title_style
        )
        self.login_sub_title.pack(pady=self.app.sub_title_padding)

        # Email label.
        self.email_label = tk.Label(
            self.root,
            text="University Email",
            **self.app.form_label_style
        )
        self.email_label.pack(pady=(5, 5))

        # Email entry field.
        self.email_entry = tk.Entry(
            self.root,
            **self.app.form_entry_style
        )
        self.email_entry.pack(pady=(0, 10))

        # Show an example email until the user starts entering one.
        self.email_placeholder = "firstname.lastname@university.com"
        self.email_entry.insert(0, self.email_placeholder)
        self.email_entry.config(fg="grey")

        # Clear or restore the placeholder when the field gains or loses focus.
        self.email_entry.bind(
            "<FocusIn>",
            lambda event: self.clear_placeholder(
                event,
                self.email_entry,
                self.email_placeholder
            )
        )

        self.email_entry.bind(
            "<FocusOut>",
            lambda event: self.show_placeholder(
                event,
                self.email_entry,
                self.email_placeholder
            )
        )

        # Password label and entry field.
        self.password_label = tk.Label(
            self.root,
            text="Password",
            **self.app.form_label_style
        )
        self.password_label.pack(pady=(5, 5))

        self.password_entry = tk.Entry(
            self.root,
            **self.app.form_entry_style
        )
        self.password_entry.pack(pady=(0, 10))

        # Use a placeholder while keeping the password visible only as placeholder text.
        self.password_placeholder = "Enter your password"
        self.password_entry.insert(0, self.password_placeholder)
        self.password_entry.config(fg="grey", show="")

        # Hide the password once the user starts entering it.
        self.password_entry.bind(
            "<FocusIn>",
            lambda event: self.clear_placeholder(
                event,
                self.password_entry,
                self.password_placeholder,
                is_password=True
            )
        )

        self.password_entry.bind(
            "<FocusOut>",
            lambda event: self.show_placeholder(
                event,
                self.password_entry,
                self.password_placeholder,
                is_password=True
            )
        )

        self.login_button = self.app.create_form_button(
            self.root,
            "Login",
            self.login_student
        )

        self.exit_button = self.app.create_form_button(
            self.root,
            "Exit",
            self.root.destroy,
            is_back=True
        )

    def login_student(self):
        email = self.email_entry.get().strip().lower()
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

        if not validate_email(email) or not validate_password(password):
            messagebox.showerror(
                "Login Failed",
                "Incorrect email or password format."
            )
            return
        
        self.app.students = self.app.database.load_students()

        # Reuse the CLI login validation logic.
        student = find_student_by_credentials(
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

        # Open the subject enrolment page for the authenticated student.
        self.app.subject_enrolment_page(student)