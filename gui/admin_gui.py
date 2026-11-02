import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from cli.utils import isValidStudentId


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
      panel, "Show All Students", self.openViewAllStudentsGUI
    )
    self.viewStudentsByGradeBtn = self.app.createMenuButton(
      panel, "Group Students by Grade", self.openViewStudentsByGradeGUI
    )
    self.viewStudentsByPassFailBtn = self.app.createMenuButton(
      panel, "Partition Students by Pass/Fail", self.openViewStudentsByPassFailGUI
    )
    self.removeStudentBtn = self.app.createMenuButton(
      panel, "Remove Student", self.openRemoveStudentGUI
    )
    self.clearStudentBtn = self.app.createMenuButton(
      panel, "Clear Database", self.clearAllStudents
    )
    self.exitButton = self.app.createMenuButton(
      panel, "Exit", self.root.destroy, isBack=True
    )

  def openViewAllStudentsGUI(self):
    self.app.clearWindow()
    self.currentPage = ViewStudentGUI(self.root, self.app)
    self.currentPage.viewStudentWindow()

  def openViewStudentsByGradeGUI(self):
    self.openStudentResultsGUI("grade")

  def openViewStudentsByPassFailGUI(self):
    self.openStudentResultsGUI("pass_fail")

  def openStudentResultsGUI(self, resultType):
    self.app.clearWindow()
    self.currentPage = ViewStudentResultsGUI(self.root, self.app, resultType)
    self.currentPage.viewResultsWindow()

  def openRemoveStudentGUI(self):
    self.app.clearWindow()
    self.currentPage = DeleteStudentGUI(self.root, self.app)
    self.currentPage.deleteStudentWindow()

  def clearAllStudents(self):
    if not self.app.database.loadStudents():
      messagebox.showinfo(
        "No Student Data",
        "There are no student records to clear.",
        parent=self.root
      )
      return

    confirmed = messagebox.askyesno(
      "Confirm Deletion",
      "This will permanently delete all student records. Are you sure?",
      parent=self.root
    )
    if not confirmed:
      return

    self.app.database.clearStudents()
    messagebox.showinfo(
      "Students Cleared",
      "All student data has been cleared.",
      parent=self.root
    )

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

    backButton = self.app.createMenuButton(
      self.root,
      "Back to Admin Menu",
      self.app.adminMenu,
      isBack=True
    )
    backButton.pack_configure(pady=(self.app.buttonPadding, 24))

class ViewStudentResultsGUI:
  gradeOrder = ("HD", "D", "C", "P", "Z", "No Subjects")
  resultOrder = ("PASS", "FAIL", "No Subjects")

  def __init__(self, root, app, resultType):
    self.root = root
    self.app = app
    self.resultType = resultType

  def viewResultsWindow(self):
    isGradeView = self.resultType == "grade"
    titleText = "Students by Grade" if isGradeView else "Students by Pass/Fail"
    title = tk.Label(
      self.root,
      text=titleText,
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
      order = self.gradeOrder if isGradeView else self.resultOrder
      groupedStudents = {category: [] for category in order}

      for student in students:
        averageMark = self.getAverageMark(student.subjects)
        if averageMark is None:
          category = "No Subjects"
        elif isGradeView:
          category = self.getGrade(averageMark)
        else:
          category = "PASS" if averageMark >= 50 else "FAIL"

        groupedStudents[category].append((student, averageMark))

      tableFrame = tk.Frame(self.root, bg=self.app.bgColor)
      tableFrame.pack(fill="both", expand=True, padx=32, pady=12)

      columns = ("category", "studentId", "name", "averageMark")
      studentTable = ttk.Treeview(
        tableFrame,
        columns=columns,
        show="headings"
      )
      studentTable.heading("category", text="Grade" if isGradeView else "Result")
      studentTable.heading("studentId", text="Student ID")
      studentTable.heading("name", text="Name")
      studentTable.heading("averageMark", text="Average Mark")
      studentTable.column("category", width=120, anchor="center")
      studentTable.column("studentId", width=140, anchor="center")
      studentTable.column("name", width=220, anchor="w")
      studentTable.column("averageMark", width=150, anchor="center")

      scrollbar = ttk.Scrollbar(
        tableFrame,
        orient="vertical",
        command=studentTable.yview
      )
      studentTable.configure(yscrollcommand=scrollbar.set)
      studentTable.pack(side="left", fill="both", expand=True)
      scrollbar.pack(side="right", fill="y")

      for category in order:
        for student, averageMark in groupedStudents[category]:
          averageText = f"{averageMark:.2f}" if averageMark is not None else "—"
          studentTable.insert(
            "",
            "end",
            values=(category, student.studentId, student.name, averageText)
          )

    backButton = self.app.createMenuButton(
      self.root,
      "Back to Admin Menu",
      self.app.adminMenu,
      isBack=True
    )
    backButton.pack_configure(pady=(self.app.buttonPadding, 24))

  @staticmethod
  def getAverageMark(subjects):
    if not subjects:
      return None
    return sum(subject["mark"] for subject in subjects) / len(subjects)

  @staticmethod
  def getGrade(mark):
    if mark >= 85:
      return "HD"
    if mark >= 75:
      return "D"
    if mark >= 65:
      return "C"
    if mark >= 50:
      return "P"
    return "Z"


class DeleteStudentGUI:
  def __init__(self, root, app):
    self.root = root
    self.app = app

  def deleteStudentWindow(self):
    title = tk.Label(
      self.root,
      text="Remove Student",
      **self.app.titleStyle
    )
    title.pack(pady=self.app.titlePadding)

    prompt = tk.Label(
      self.root,
      text="Enter the 6-digit student ID to remove.",
      **self.app.subTitleStyle
    )
    prompt.pack(pady=self.app.subTitlePadding)

    validateCommand = (self.root.register(self.validateStudentIdInput), "%P")
    self.studentIdEntry = tk.Entry(
      self.root,
      validate="key",
      validatecommand=validateCommand,
      **self.app.formEntryStyle
    )
    self.studentIdEntry.pack(pady=(0, 12))

    # validation label for invalid student ID input under the input field
    self.studentIdValidationMessage = tk.Label(
      self.root,
      text="",
      font=self.app.messageFont,
      bg=self.app.bgColor,
      fg="#F87171"
    )
    self.studentIdValidationMessage.pack(pady=(0, 8))

    self.app.createFormButton(
      self.root,
      "Remove Student",
      self.removeStudent
    )
    self.app.createFormButton(
      self.root,
      "Back to Admin Menu",
      self.app.adminMenu,
      isBack=True
    )

  # validate student ID input
  # number only, max length 6
  def validateStudentIdInput(self, proposedValue):
    if not proposedValue:
      self.studentIdValidationMessage.config(text="")
      return True

    if not proposedValue.isascii() or not proposedValue.isdigit():
      self.studentIdValidationMessage.config(text="Numbers only.")
      return False

    if len(proposedValue) > 6:
      self.studentIdValidationMessage.config(text="Student ID must be at most 6 digits.")
      return False

    self.studentIdValidationMessage.config(text="")
    return True

  def removeStudent(self):
    studentId = self.studentIdEntry.get().strip()
    if not isValidStudentId(studentId):
      messagebox.showerror(
        "Invalid Student ID",
        "Please enter a 6-digit ID.",
        parent=self.root
      )
      return

    student = self.app.database.getStudent(studentId)
    if student is None:
      messagebox.showerror(
        "Student Not Found",
        f"No student found with ID {studentId}.",
        parent=self.root
      )
      return

    confirmed = messagebox.askyesno(
      "Confirm Deletion",
      f"Are you sure you want to delete {student.name} "
      f"({student.studentId})?",
      parent=self.root
    )
    if not confirmed:
      return

    if not self.app.database.deleteStudent(student.studentId):
      messagebox.showerror(
        "Deletion Failed",
        f"Student with ID {student.studentId} could not be found.",
        parent=self.root
      )
      return

    messagebox.showinfo(
      "Student Deleted",
      f"Student {student.name} ({student.studentId}) has been deleted.",
      parent=self.root
    )
    self.app.adminMenu()
