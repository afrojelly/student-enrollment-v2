import tkinter as tk
from tkinter import messagebox

class UniAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry ("1000x600") # Set the window size to 1000 pixels wide and 600 pixels tall, providing a spacious area for the GUI components.
        self.root.title ("University Enrollment System") # Set the title of the window to "University Enrollment System", which will appear in the title bar of the window.

    #GUI colour in the background of the window, enhancing the visual appeal and providing a consistent look and feel for the application.
        self.bgColor = "#101827"#background colour.
        self.panelColor= "#1C2A40" #로그인 pannel이나 기타 pannel에 사용
        self.buttoncolor = "#3778D6"
        self.exitButtonColor = "#556276" #exit 버튼은 다른색으로 했어요! 
        self.buttonFG = "#010101"  #button 내부글자 colour 
        self.buttonActive = "#475D7A"
        self.textColor = "#E2E8F0"
        self.subTextColor = "#A0AEC0"
    #GUI Font setting 
        self.mainTitleFont = ("Arial", 25, "bold")
        self.subTitleFont = ("Arial", 20)
        self.buttonFont = ("Arial", 18, "bold")
        self.messageFont = ("Arial", 14)  #error message

        self.root.configure(bg=self.bgColor)
        self.mainMenu()

        #mainTitle: 25
        #subTitle:20
        #button: 20

    def clearWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mainMenu(self):
        self.clearWindow() # Clear the window before adding new widgets; tkinter does not automatically clear previous widgets when switching between different screens or menus. This method ensures that the window is clean and ready for new content, preventing overlapping or cluttered interfaces.
        
        #mainmenu title and subtitle
        self.mainMenuTitle = tk.Label( #main title of the main menu, welcoming users to the University Enrollment System. The title is styled with a larger font size and bold weight to make it stand out.
                self.root, 
                text="Welcome to the University Enrollment System", 
                font=self.mainTitleFont,
                bg=self.bgColor,
                fg=self.textColor
            )
        self.mainMenuTitle.pack (pady=(30,10))
        
        self.mainMenuSubtitle = tk.Label( #sub title of the main menu, providing instructions to users on how to proceed. It is styled with a slightly smaller font size than the main title and is positioned below it with some padding for visual separation.
                self.root,
                text="Please choose an option below to access the system",
                font=self.subTitleFont,
                bg=self.bgColor,
                fg=self.subTextColor
            )
        self.mainMenuSubtitle.pack(pady=(0,20))

#system access buttons, allowing users to navigate to the Admin or Student sections of the application. Each button is styled with a consistent width and is linked to a specific command that opens the corresponding window when clicked.
        self.adminButton = tk.Button(
            self.root, 
            text="Admin", 
            font=self.buttonFont,
            width = 40,
            bg=self.buttoncolor,
            fg=self.buttonFG,
            activebackground=self.buttonActive,

            command=self.adminMenu)
        self.adminButton.pack(pady=10, ipady=15) #pady = 사이간격 ipady = button 세로

        self.studentButton = tk.Button(
            self.root,
            text="Student",
            font=self.buttonFont,
            width=40,
            bg=self.buttoncolor,
            fg=self.buttonFG,
            activebackground=self.buttonActive,

            command=self.studentMenu)
        self.studentButton.pack(pady=10, ipady=15)

        self.exitButton = tk.Button(
            self.root,
            text="Exit",
            font= self.buttonFont,
            width=40,
            bg=self.exitButtonColor,
            fg=self.buttonFG,   
            activebackground=self.buttonActive,

            command=self.root.destroy) # page exit  
        self.exitButton.pack(pady=10, ipady=15)

#Admin menu
    def adminMenu(self):
        messagebox.showinfo(
            "Admin System",
            "Admin GUI is not implemented yet."
        )

#student Menu
    def studentMenu(self):
        self.clearWindow()      
        # Code to open the student window
        self.studentMenuTitle = tk.Label(
            self.root, 
            text="Welcome to the Student System", 
            font=self.mainTitleFont,
            bg=self.bgColor,
            fg=self.textColor
        )    

        self.studentMenuTitle.pack(pady=(30,10))

        self.studentMenuSubtitle = tk.Label( #sub title of the main menu, providing instructions to users on how to proceed. It is styled with a slightly smaller font size than the main title and is positioned below it with some padding for visual separation.
                self.root,
                text="Please choose an option below to access the functionality",
                font=self.subTitleFont,
                bg=self.bgColor,
                fg=self.subTextColor
            )
        self.studentMenuSubtitle.pack(pady=(0,20))

        #student menu buttons and options, allowing users to navigate to the login or registration sections of the student system. Each button is styled with a consistent width and is linked to a specific command that opens the corresponding window when clicked.
        self.loginButton = tk.Button(
            self.root, 
            width=40,
            text="Login", 
            font=self.buttonFont,
            bg=self.buttoncolor,
            fg=self.buttonFG,
            activebackground=self.buttonActive,
            
            command=self.loginPage)
        self.loginButton.pack(pady=10, ipady=15)

        self.registerButton = tk.Button(
            self.root, 
            width=40,
            text="Register", 
            font=self.buttonFont,
            bg=self.buttoncolor,
            fg=self.buttonFG,
            activebackground=self.buttonActive,

            command=self.registrationPage)
        self.registerButton.pack(pady=10, ipady=15)

        self.exitButton = tk.Button(
            self.root,
            width=40,
            text="Back to Main Menu",
            font=self.buttonFont,
            bg=self.exitButtonColor,
            fg=self.buttonFG,
            activebackground=self.buttonActive,

            command=self.mainMenu) #one page back to main menu
        self.exitButton.pack(pady=10, ipady=15) 

    def loginPage(self):
            messagebox.showinfo(
                "Student Login",
                "Login GUI is not implemented yet."
            )

    def registrationPage(self):
            messagebox.showinfo(
                "Student Registration",
                "Registration GUI is not implemented yet."
            )

if __name__ == "__main__":
    root = tk.Tk() 
    #gui root window is created using the Tk() constructor from the tkinter library. This root window serves as the main application window where all other GUI components will be placed.
    app = UniAppGUI(root)
    root.mainloop()

#pady=5 ~ pady=10: 버튼이나 텍스트 입력창처럼 요소들이 서로 조밀하게 모여 있어야 할 때 사용합니다.
#pady=15 ~ pady=20: 일반적인 위젯 간 기본 여백으로 가장 무난하고 보기 좋습니다.
# pady=30 이상: 화면 제일 위의 제목(Title)처럼 다른 요소들과 크게 구분 짓고 싶을 때 사용합니다.