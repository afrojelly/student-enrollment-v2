import tkinter as tk
from tkinter import messagebox

from cli.change_password import update_password, verify_password


class ChangePasswordGUI:
    def __init__(self, root, app, student):
        self.root = root
        self.app = app
        self.student = student

    def change_password_window(self):
        self.app.clear_window()
        self.password_title = tk.Label(
            self.root,
            text="Would you like to change your password?",
            **self.app.title_style
        )
        self.password_title.pack(pady=self.app.title_padding)

        self.password_subtitle = tk.Label(
            self.root,
            text=f"Please verify your current password, {self.student.name}",
            **self.app.sub_title_style
        )
        self.password_subtitle.pack(pady=self.app.sub_title_padding)

        # Verify the current password.
        self.current_password_label = tk.Label(
            self.root,
            text="Current Password",
            **self.app.form_label_style
        )
        self.current_password_label.pack(pady=(5, 5))

        self.current_password_entry = tk.Entry(
            self.root,
            **self.app.form_entry_style,
            show="*"  # Hide the password; remove this option to display it.
        )
        self.current_password_entry.pack(pady=(0, 10))

        self.verify_button = self.app.create_form_button(
            self.root,
            "Verify",
            self.verify_current_password
        )

        # Back Button
        self.exit_button = self.app.create_form_button(
            self.root,
            "Exit",
            self.exit_change_password,
            is_back=True
        )

    # Return to the subject enrolment page.
    def exit_change_password(self):
        self.app.subject_enrolment_page(self.student)

    # Verify the current password before allowing a change.
    def verify_current_password(self):
        current_password = self.current_password_entry.get()

        if not current_password:
            messagebox.showerror(
                "Password Required",
                "Please enter your current password."
            )
            return

        if not verify_password(self.student, current_password):
            messagebox.showerror(
                "Verification Failed",
                "Current password is incorrect. Please try again."
            )
            return

        self.new_password()

    # After verification, show the page for entering a new password.
    def new_password(self):
        self.app.clear_window()

        self.new_password_title = tk.Label(
            self.root,
            text="Please enter your new password",
            **self.app.sub_title_style
        )
        self.new_password_title.pack(pady=self.app.title_padding)

        self.new_password_label = tk.Label(
            self.root,
            text="New Password",
            **self.app.form_label_style
        )
        self.new_password_label.pack(pady=(5, 5))

        self.new_password_entry = tk.Entry(
            self.root,
            **self.app.form_entry_style,
            show="*"
        )
        self.new_password_entry.pack(pady=(0, 5))

        self.password_hint = tk.Label(
            self.root,
            text="Uppercase first | More than 5 letters | At least 3 digits",
            **self.app.hint_style
        )
        self.password_hint.pack(pady=(0, 10))

        self.confirm_password_label = tk.Label(
            self.root,
            text="Confirm New Password",
            **self.app.form_label_style
        )
        self.confirm_password_label.pack(pady=(5, 5))

        self.confirm_password_entry = tk.Entry(
            self.root,
            **self.app.form_entry_style,
            show="*"
        )
        self.confirm_password_entry.pack(pady=(0, 15))

        self.confirm_button = self.app.create_form_button(
            self.root,
            "Confirm",
            self.save_new_password
        )

        self.exit_button = self.app.create_form_button(
            self.root,
            "Exit",
            self.exit_change_password,
            is_back=True
        )

    # Save the new password after validation and confirmation.
    def save_new_password(self):
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        result = update_password(
            self.student,
            self.app.students,
            self.app.database,
            new_password,
            confirm_password
        )

        if result == "success":
            messagebox.showinfo(
                "Password Changed Successfully",
                "Please use your new password the next time you log in."
            )
            self.exit_change_password()

        elif result == "invalid":
            messagebox.showerror(
                "Invalid Password",
                "Password must start with an uppercase letter,\n"
                "contain at more than 5 letters and at least 3 digits."
            )
        elif result == "mismatch":
            messagebox.showerror(
                "Password Mismatch",
                "Passwords do not match. Please try again."
            )
        elif result == "saveError":
            messagebox.showerror(
                "Database Error",
                "Unable to save the new password."
            )
        else:
            messagebox.showerror(
                "Change Password Failed",
                "Unable to update your password."
            )