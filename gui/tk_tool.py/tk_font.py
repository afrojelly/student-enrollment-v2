import tkinter as tk
from tkinter import font

# Initialize Tkinter (Required)
root = tk.Tk()

# Retrieve and sort available font families
available_fonts = list(font.families())
available_fonts.sort()

# Print the list
for f in available_fonts:
    print(f)
