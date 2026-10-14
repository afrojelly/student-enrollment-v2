import tkinter as tk
from tkinter import messagebox 


class subjectEnrolmentGUI:
    def __init__(self, root, app, student):
        self.root = root
        self.app = app
        self.student = student

    def enrolmentWindow(self):
        student = self.student

        