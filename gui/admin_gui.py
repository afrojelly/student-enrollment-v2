import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk

class AdminGUI:
  def __init__(self, root, app):
    self.root = root
    self.app = app

  def adminWindow(self):
    self.adminMenuTitle = tk.Label(
      self.root,
      text = "Welcome to the Admin System",
      **self.app.titleStyle
    )

    self.adminMenuTitle.pack(
      pady = self.app.titlePadding
    )

    self.adminMenuSubtitle = tk.Label(
      self.root,
      text = "Please choose an option below.",
      **self.app.subTitleStyle
    )

    self.adminMenuSubtitle.pack(
      pady = self.app.subTitlePadding
    )

    panel = self.app.createMenuPanel()
    self.viewStudentsAllBtn = self.app.createMenuButton(
      panel, "View All Students", self.openViewAllStudentsGUI
    )
    self.viewStudentsByGradeBtn = self.app.createMenuButton(
      panel, "View Students by Grade", self.showViewNotImplemented
    )
    self.viewStudentsByPassFailBtn = self.app.createMenuButton(
      panel, "View Students by Pass/Fail", self.showViewNotImplemented
    )
    self.deleteStudentBtn = self.app.createMenuButton(
      panel, "Delete Student by ID", self.openDeleteStudentGUI
    )
    self.clearStudentBtn = self.app.createMenuButton(
      panel, "Clear All Students", self.openClearStudentGUI
    )
    self.exitButton = self.app.createMenuButton(
      panel, "Exit", self.root.destroy, isBack=True
    )


  def openViewAllStudentsGUI(self):
    self.app.clearWindow()
    self.currentPage = ViewStudentGUI(self.root, self.app)
    self.currentPage.viewStudentWindow()

  def showViewNotImplemented(self):
    mb.showinfo("Not available yet", "This student view is not implemented yet.")

  def openDeleteStudentGUI(self):
    self.currentPage = DeleteStudentGUI(self.root, self.app)

  def openClearStudentGUI(self):
    self.currentPage = ClearStudentGUI(self.root, self.app)

class ViewStudentGUI:
  def __init__(self, root, app):
    self.root = root
    self.app = app

  def viewStudentWindow(self):
    title = tk.Label(
      self.root,
      text="All Students",
      **self.app.titleStyle
    )
    title.pack(pady=self.app.titlePadding)

    students = self.app.database.loadStudents()

    if not students:
      emptyMessage = tk.Label(
        self.root,
        text="No students registered.",
        **self.app.subTitleStyle
      )
      emptyMessage.pack(pady=self.app.subTitlePadding)
    else:
      tableFrame = tk.Frame(self.root, bg=self.app.bgColor)
      tableFrame.pack(fill="both", expand=True, padx=32, pady=12)

      columns = ("studentId", "name", "email")
      studentTable = ttk.Treeview(
        tableFrame,
        columns=columns,
        show="headings"
      )
      studentTable.heading("studentId", text="Student ID")
      studentTable.heading("name", text="Name")
      studentTable.heading("email", text="Email")
      studentTable.column("studentId", width=140, anchor="center")
      studentTable.column("name", width=220, anchor="w")
      studentTable.column("email", width=360, anchor="w")

      scrollbar = ttk.Scrollbar(
        tableFrame,
        orient="vertical",
        command=studentTable.yview
      )
      studentTable.configure(yscrollcommand=scrollbar.set)
      studentTable.pack(side="left", fill="both", expand=True)
      scrollbar.pack(side="right", fill="y")

      for student in students:
        studentTable.insert(
          "",
          "end",
          values=(student.studentId, student.name, student.email)
        )

    self.app.createMenuButton(
      self.root,
      "Back to Admin Menu",
      self.app.adminMenu,
      isBack=True
    )
class DeleteStudentGUI:
  def __init__(self, root, app):
    self.root = root
    self.app = app

class ClearStudentGUI:
  def __init__(self, root, app):
    self.root = root
    self.app = app