import tkinter as tk
from gui.login_gui import LoginGUI
from gui.registration_gui import RegistrationGUI


class StudentGUI:
    def __init__(self, root, app):
        self.root = root
        self.app = app

    def student_window(self):
        self.student_menu_title = tk.Label(
            self.root,
            text="Welcome to the Student System",
            **self.app.title_style
        )
        self.student_menu_title.pack(
            pady=self.app.title_padding
        )

        self.student_menu_subtitle = tk.Label(
            self.root,
            text="Please choose an option below to access the functionality",
            **self.app.sub_title_style
        )
        self.student_menu_subtitle.pack(
            pady=self.app.sub_title_padding
        )

        panel = self.app.create_menu_panel()
        self.login_button = self.app.create_menu_button(panel, "Login", self.login_page)
        self.register_button = self.app.create_menu_button(panel, "Register", self.registration_page)
        self.exit_button = self.app.create_menu_button(panel, "Back to Main Menu", self.app.main_menu, is_back=True)


    def login_page(self):
        self.app.clear_window()

        login = LoginGUI(
            self.root,
            self.app
        )
        login.login_window()

   
    def registration_page(self):
        self.app.clear_window()

        registration = RegistrationGUI(
            self.root,
            self.app
        )
        registration.regi_window()