import tkinter as tk

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
      panel, "View All Students", self.openViewStudentGUI
    )
    self.viewStudentsByGradeBtn = self.app.createMenuButton(
      panel, "View Students by Grade", self.openViewStudentGUI
    )
    self.viewStudentsByPassFailBtn = self.app.createMenuButton(
      panel, "View Students by Pass/Fail", self.openViewStudentGUI
    )
    self.deleteStudentBtn = self.app.createMenuButton(
      panel, "Delete Student by ID", self.openDeleteStudentGUI
    )
    self.clearStudentBtn = self.app.createMenuButton(
      panel, "Clear All Students", self.openClearStudentGUI
    )

  def openViewStudentGUI(self):
    self.currentPage = ViewStudentGUI(self.root, self.app)

  def openDeleteStudentGUI(self):
    self.currentPage = DeleteStudentGUI(self.root, self.app)

  def openClearStudentGUI(self):
    self.currentPage = ClearStudentGUI(self.root, self.app)

class ViewStudentGUI:
  def __init__(self, root, app):
    self.root = root
    self.app = app

class DeleteStudentGUI:
  def __init__(self, root, app):
    self.root = root
    self.app = app

class ClearStudentGUI:
  def __init__(self, root, app):
    self.root = root
    self.app = app