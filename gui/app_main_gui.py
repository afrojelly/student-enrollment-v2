
from cli.database import Database

import tkinter as tk
from gui.gui_style import GUIStyle
from gui.subject_enrolment_gui import SubjectEnrolmentGUI
from gui.login_gui import LoginGUI


class UniAppGUI(GUIStyle):
    def __init__(self, root):
        super().__init__()

# Main Tkinter window
        self.root = root
        self.root.geometry("1000x800")
        self.root.title("University Enrollment System")

        # Connect GUI to existing CLI Database
        self.database = Database()
        self.students = self.database.load_students()

        # Currently logged-in student
        self.current_student = None

        self.root.configure(bg=self.bg_color)

        # Start GUI from Login Page
        self.login_page()

# Login Page - starting window
    def login_page(self):
        self.clear_window()

        login = LoginGUI(
            self.root,
            self
        )
        login.login_window()

# Subject Enrolment Page - after successful login
    def subject_enrolment_page(self, student):
        self.current_student = student
        self.clear_window()

        enrolment = SubjectEnrolmentGUI(
            self.root,
            self,
            student
        )
        enrolment.enrolment_window()

#Logout - return to Login Page
    def logout(self):
        self.current_student = None
        self.login_page()

# Clear current window before opening the next page
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = UniAppGUI(root)
    root.mainloop()
