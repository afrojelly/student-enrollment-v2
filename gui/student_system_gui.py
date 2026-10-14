import tkinter as tk
from gui.login_gui import loginGUI
from gui.registration_gui import registrationGUI


class studentGUI:
    def __init__(self, root, app):
        self.root = root
        self.app = app

    def studentWindow(self):
        self.studentMenuTitle = tk.Label(
            self.root,
            text="Welcome to the Student System",
            **self.app.titleStyle
        )
        self.studentMenuTitle.pack(
            pady=self.app.titlePadding
        )

        self.studentMenuSubtitle = tk.Label(
            self.root,
            text="Please choose an option below to access the functionality",
            **self.app.subTitleStyle
        )
        self.studentMenuSubtitle.pack(
            pady=self.app.subTitlePadding
        )

        panel = self.app.createMenuPanel()
        self.loginButton = self.app.createMenuButton(panel, "Login", self.loginPage)
        self.registerButton = self.app.createMenuButton(panel, "Register", self.registrationPage)
        self.exitButton = self.app.createMenuButton(panel, "Back to Main Menu", self.app.mainMenu, isBack=True)


    def loginPage(self):
        self.app.clearWindow()

        login = loginGUI(
            self.root,
            self.app
        )
        login.loginWindow()

   
    def registrationPage(self):
        self.app.clearWindow()

        registration = registrationGUI(
            self.root,
            self.app
        )
        registration.regiWindow()