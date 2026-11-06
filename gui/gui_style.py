import tkinter as tk


class GUIStyle:
    def __init__(self):
        # Background colors used throughout the application.
        self.bg_color = "#101827"
        self.panel_color = "#1C2A40"  # Used for login panels and other panels.
        self.button_color = "#3778D6"
        self.exit_button_color = "#556276"  # Back and exit buttons use a different color.
        self.button_active = "#475D7A"
        self.button_fg = "#010101"  # Button text color.
        self.text_color = "#E2E8F0"  # Main text color.
        self.sub_text_color = "#A0AEC0"

        # Font settings.
        self.main_title_font = ("Noto Sans KR", 25, "bold")
        self.sub_title_font = ("Noto Sans KR", 20)
        self.button_font = ("Noto Sans KR", 18, "bold")
        self.message_font = ("Noto Sans KR", 14)  # Used for messages and form fields.

        # Spacing settings.
        self.title_padding = (34, 8)
        self.sub_title_padding = (0, 22)
        self.button_padding = 8
        self.button_size_padding = 5

        # Widget style dictionaries are passed to Tkinter with the ** operator.
        self.title_style = {  # Main title style.
            "font": self.main_title_font,
            "bg": self.bg_color,
            "fg": self.text_color,
        }

        self.sub_title_style = {  # Subtitle style.
            "font": self.sub_title_font,
            "bg": self.bg_color,
            "fg": self.sub_text_color,
        }

        self.button_style = {  # Large buttons for pages without input fields.
            "width": 40,
            "font": self.button_font,
            "fg": self.button_fg,
            "activebackground": self.button_active,
        }

        self.form_button_style = {  # Smaller buttons for forms, such as login and registration.
            "width": 25,
            "height": 2,
            "font": self.message_font,
            "fg": self.button_fg,
            "activebackground": self.button_active,
        }

        # Styles for labels that describe form fields.
        self.form_label_style = {
            "font": self.message_font,
            "bg": self.panel_color,
            "fg": self.text_color,
        }

        # Style for text-entry fields where users enter data.
        self.form_entry_style = {
            "font": self.message_font,
            "width": 35,
            "bg": "#FFFFFF",
            "fg": self.bg_color,
        }

        # Style for hints that explain input requirements.
        self.hint_style = {
            "font": ("Bahnschrift", 10),
            "bg": self.bg_color,
            "fg": self.sub_text_color,
        }

    def create_menu_panel(self):
        # Create a colored panel to visually distinguish the menu.
        panel = tk.Frame(self.root, bg=self.panel_color, padx=32, pady=24)
        panel.pack()
        return panel

    def create_menu_button(self, parent, text, command, is_back=False):
        # Use a distinct color for back or exit buttons.
        if is_back:
            color = self.exit_button_color
        else:
            color = self.button_color

        # Create a large button for menu pages without input fields.
        button = tk.Button(
            parent,
            text=text,
            bg=color,
            command=command,
            **self.button_style
        )
        button.pack(
            pady=self.button_padding,
            ipady=self.button_size_padding
        )
        return button

    # Create a smaller button for form pages, such as login and registration.
    def create_form_button(self, parent, text, command, is_back=False):
        # Use a distinct color for back or exit buttons.
        if is_back:
            color = self.exit_button_color
        else:
            color = self.button_color

        # Apply the shared form-button style.
        button = tk.Button(
            parent,
            text=text,
            bg=color,
            command=command,
            **self.form_button_style
        )
        button.pack(pady=5)
        return button