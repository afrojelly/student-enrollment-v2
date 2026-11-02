class GUIStyle:
    def __init__(self):

    #GUI colour in the background of the window, enhancing the visual appeal and providing a consistent look and feel for the application.
        self.bg_color = "#101827"#background colour.
        self.panel_color= "#1C2A40" #로그인 pannel이나 기타 pannel에 사용
        self.button_color = "#3778D6"
        self.exit_button_color = "#556276" #exit 버튼은 다른색으로 했어요!
        self.button_active = "#475D7A"
        self.button_fg = "#010101"  #button 내부글자 colour
        self.text_color = "#E2E8F0" #일반 text colour
        self.sub_text_color = "#A0AEC0"
    
    #GUI Font setting 
        self.main_title_font = ("Noto Sans KR", 25, "bold")
        self.sub_title_font = ("Noto Sans KR", 20)
        self.button_font = ("Noto Sans KR", 18, "bold")
        self.message_font = ("Noto Sans KR", 14)  #error message #data입력필드
    
    #GUI spacing option 
        self.title_padding = (34, 8)
        self.sub_title_padding = (0, 22)
        self.button_padding = 8
        self.button_size_padding = 5

# GUI form button settings. Expand a style dictionary with **self.title_style.
        self.title_style = { #main title
            "font": self.main_title_font,
            "bg": self.bg_color,
            "fg": self.text_color
        }

        self.sub_title_style = { #subtitle format
            "font": self.sub_title_font,
            "bg": self.bg_color,
            "fg": self.sub_text_color
        }

        self.button_style = { #main size button -> 버튼만 있는 페이지에서 사용하는 큰 사이즈 버튼
            "width": 40,
            "font": self.button_font,
            "fg": self.button_fg,
            "activebackground": self.button_active
        }
            
        
        self.form_button_style = { #small size button -> 레지 페이지나 로그인 페이지에서 , 위쪽에 입력 있고 아래에 confirm 이나 cancle등을 넣을때 쓰는 작은 버튼)
            "width": 25,
            "height": 2,
            "font": self.message_font,
            "fg": self.button_fg,
            "activebackground": self.button_active
        }

#tk.label: 입력항목-보여주는거,
        self.form_label_style = {
            "font": self.message_font,
            "bg":self.panel_color,
            "fg":self.text_color
        }

# tk.Entry: 실체 사용자 입력칸
        self.form_entry_style = {
            "font": self.message_font,
            "width":35,
            "bg": "#FFFFFF",
            "fg": self.bg_color,
        }

# Small hint text for registration/login input rules
        self.hint_style = {
            "font": ("Bahnschrift", 10),
            "bg": self.bg_color,
            "fg": self.sub_text_color
        }

        # Main title: 25
        # Subtitle: 20
        #button: 20