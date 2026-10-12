class GUIStyle:
    def __init__(self):

    #GUI colour in the background of the window, enhancing the visual appeal and providing a consistent look and feel for the application.
        self.bgColor = "#0F1E3A"#background colour.
        self.panelColor= "#1E2F4F" #로그인 pannel이나 기타 pannel에 사용
        self.buttonColor = "#A7B6D0"
        self.exitButtonColor = "#D8D8DB" #exit 버튼은 다른색으로 했어요! 
        self.buttonActive = "#1E2F4F"
        self.buttonFG = "#0F1E3A"  #button 내부글자 colour 
        self.textColor = "#FFFFFF" #일반 text colour 
        self.subTextColor = "#A7B6D0"
    #GUI Font setting 
        self.mainTitleFont = ("Bahnschrift", 25, "bold")
        self.subTitleFont = ("Bahnschrift", 16)
        self.buttonFont = ("Bahnschrift", 17, "bold")
        self.messageFont = ("Bahnschrift", 14)  #error message #data입력필드 
    #GUI spacing 
        self.titlePadding = (34, 8)
        self.subTitlePadding = (0, 22)
        self.buttonPadding = 8
        self.buttonSizePadding = 9

# GUI Form Button Settings- Widget Style Settings => format은 한번에 다 불러오려면 **self.titleStyle 이런식으로 앞에 **(별두개!)
        self.titleStyle = { #main title 
            "font": self.mainTitleFont,
            "bg": self.bgColor,
            "fg": self.textColor
        }

        self.subTitleStyle = { #subtitle format 
            "font": self.subTitleFont,
            "bg": self.bgColor,
            "fg": self.subTextColor
        }

        self.buttonStyle = { #main size button -> 버튼만 있는 페이지에서 사용하는 큰 사이즈 버튼 )
            "width": 40,
            "font": self.buttonFont,
            "fg": self.buttonFG,
            "activebackground": self.buttonActive
        }
            
        
        self.formButtonStyle = { #small size button -> 레지 페이지나 로그인 페이지에서 , 위쪽에 입력 있고 아래에 confirm 이나 cancle등을 넣을때 쓰는 작은 버튼)
            "width": 25,
            "height": 2,
            "font": self.messageFont,
            "fg": self.buttonFG,
            "activebackground": self.buttonActive
        }


        #mainTitle: 25
        #subTitle:20
        #button: 20