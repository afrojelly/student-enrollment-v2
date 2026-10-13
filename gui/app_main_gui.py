from cli.database import Database # import existing CLI database to the GUI  

import tkinter as tk
from tkinter import messagebox
from gui.registration_gui import registrationGUI
from gui.gui_style import GUIStyle


class UniAppGUI(GUIStyle):
    def __init__(self, root):
        super().__init__() #UniAppGUI가 GUIStyle을 상속 (inheritence) ->UniAppGUI가 GUIStyle의 속성들을 사용가능
        
        self.root = root #THkinter GUI 의 가장 바탕, 최상위 main window창
        self.root.geometry ("1000x600") # Set the window size to 1000 pixels wide and 600 pixels tall, providing a spacious area for the GUI components.
        self.root.title ("University Enrollment System") # Set the title of the window to "University Enrollment System", which will appear in the title bar of the window.

#connect GUI to the existing database from CLI 
        self.database = Database() #실제 Students.data 파일 관리 -> self.app.database 로 불러오기 가능 
        self.students = self.database.loadStudents()
        
        self.root.configure(bg=self.bgColor)
        self.mainMenu()

        #mainTitle: 25
        #subTitle:20
        #button: 20

    def clearWindow(self):
        for widget in self.root.winfo_children(): #현재 GUI 창 내의 모든 widget clear => Widget = tkinter base window component, including labe, button, entry, frame....etc.
            widget.destroy()

    def createMenuPanel(self):
        # A coloured panel makes the menu stand out without extra packages.
        panel = tk.Frame(self.root, bg=self.panelColor, padx=32, pady=24) #pixel
        panel.pack()
        return panel

#Button만드는 함수 - 이거는 main button, button만 있는 페이지 
    def createMenuButton(self, parent, text, command, isBack=False):
        if isBack:
            color = self.exitButtonColor  
        else:
            color = self.buttonColor #button colour

        button = tk.Button(
            parent,
            text=text,
            bg=color,
            command=command,
            **self.buttonStyle
        )
        button.pack(
            pady=self.buttonPadding, 
            ipady=self.buttonSizePadding
            )
        return button

# Create small button for input form pages
#이거는 button -입력창 (form) 이 있는 페이지의 작은사이즈의 버튼 (registration and login )
    def createFormButton (self, parent, text, command, isBack=False):
        if isBack:
            color = self.exitButtonColor  
        else:
            color = self.buttonColor

        button = tk.Button(
            parent,
            text=text,
            bg=color,
            command=command,
            **self.formButtonStyle
        )
        button.pack(pady=5)
        return button



    def mainMenu(self):
        self.clearWindow() # Clear the window before adding new widgets; tkinter does not automatically clear previous widgets when switching between different screens or menus. This method ensures that the window is clean and ready for new content, preventing overlapping or cluttered interfaces.    
#mainmenu title and subtitle
        
        self.mainMenuTitle = tk.Label( #main title of the main menu, welcoming users to the University Enrollment System. The title is styled with a larger font size and bold weight to make it stand out.
                self.root, 
                text="Welcome to the University Enrollment System", 
                **self.titleStyle
            )
        self.mainMenuTitle.pack (
            pady=self.titlePadding
            )       
        self.mainMenuSubtitle = tk.Label( #sub title of the main menu, providing instructions to users on how to proceed. It is styled with a slightly smaller font size than the main title and is positioned below it with some padding for visual separation.
                self.root,
                text="Please choose an option below to access the system",
                **self.subTitleStyle
            )
        self.mainMenuSubtitle.pack(
            pady=self.subTitlePadding
            )
        
#system access buttons, 
# #allowing users to navigate to the Admin or Student sections of the application. 
# #Each button is styled with a consistent width and is linked to a specific command that opens the corresponding window when clicked.
#the button specification (panel (:on the panel), "Admin (showing on button)", Command (:action))
        panel = self.createMenuPanel() #button 하이라이트 시켜주는 패넬을 만들어서 넣어봤어요 
        self.adminButton = self.createMenuButton (panel, "Adimin", self.adminMenu)
        self.studentButton = self.createMenuButton(panel,"Student", self.studentMenu)
        self.exitButton = self.createMenuButton(panel, "Exit", self.root.destroy, isBack=True)


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
            **self.titleStyle
        )    
        self.studentMenuTitle.pack(
            pady=self.titlePadding
            )

        self.studentMenuSubtitle = tk.Label( #sub title of the main menu, providing instructions to users on how to proceed. It is styled with a slightly smaller font size than the main title and is positioned below it with some padding for visual separation.
                self.root,
                text="Please choose an option below to access the functionality",
                **self.subTitleStyle
            )
        self.studentMenuSubtitle.pack(
            pady=self.subTitlePadding
            )
#student menu buttons and options, allowing users to navigate to the login or registration sections of the student system. Each button is styled with a consistent width and is linked to a specific command that opens the corresponding window when clicked.
        panel = self.createMenuPanel()
        self.loginButton = self.createMenuButton(panel, "Login", self.loginPage)
        self.registerButton = self.createMenuButton(panel, "Register", self.registrationPage)
        self.exitButton = self.createMenuButton(panel, "Back to Main Menu", self.mainMenu, isBack=True)


    def loginPage(self):
            messagebox.showinfo(
                "Student Registration",
                "Registration GUI is not implemented yet."
            )

   
    def registrationPage(self):
        self.clearWindow()

        registration = registrationGUI(
            self.root,
            self
        )
        registration.regiWindow()

if __name__ == "__main__":
    root = tk.Tk() 
    #gui root window is created using the Tk() constructor from the tkinter library. This root window serves as the main application window where all other GUI components will be placed.
    app = UniAppGUI(root) ###    def __init__(self, root, backCommand, app) 해주시면, app자체가 UniAppGUI 객체 자체를 나타내서, app 매개변수로 받을 수 있음 
    root.mainloop()

#pady=5 ~ pady=10: 버튼이나 텍스트 입력창처럼 요소들이 서로 조밀하게 모여 있어야 할 때 사용합니다.
#pady=15 ~ pady=20: 일반적인 위젯 간 기본 여백으로 가장 무난하고 보기 좋습니다.
# pady=30 이상: 화면 제일 위의 제목(Title)처럼 다른 요소들과 크게 구분 짓고 싶을 때 사용합니다.