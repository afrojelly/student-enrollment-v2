import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from cli.utils import is_valid_student_id


class AdminGUI:
  def __init__(self, root, app):
    self.root = root
    self.app = app

  def admin_window(self):
    self.admin_menu_title = tk.Label(
      self.root,
      text = "Welcome to the Admin System",
      **self.app.title_style
    )

    self.admin_menu_title.pack(
      pady = self.app.title_padding
    )

    self.admin_menu_subtitle = tk.Label(
      self.root,
      text = "Please choose an option below.",
      **self.app.sub_title_style
    )

    self.admin_menu_subtitle.pack(
      pady = self.app.sub_title_padding
    )

    panel = self.app.create_menu_panel()
    self.view_students_all_btn = self.app.create_menu_button(
      panel, "Show All Students", self.open_view_all_students_gui
    )
    self.view_students_by_grade_btn = self.app.create_menu_button(
      panel, "Group Students by Grade", self.open_view_students_by_grade_gui
    )
    self.view_students_by_pass_fail_btn = self.app.create_menu_button(
      panel, "Partition Students by Pass/Fail", self.open_view_students_by_pass_fail_gui
    )
    self.remove_student_btn = self.app.create_menu_button(
      panel, "Remove Student", self.open_remove_student_gui
    )
    self.clear_student_btn = self.app.create_menu_button(
      panel, "Clear Database", self.clear_all_students
    )
    self.exit_button = self.app.create_menu_button(
      panel, "Exit", self.root.destroy, is_back=True
    )

  def open_view_all_students_gui(self):
    self.app.clear_window()
    self.current_page = ViewStudentGUI(self.root, self.app)
    self.current_page.view_student_window()

  def open_view_students_by_grade_gui(self):
    self.open_student_results_gui("grade")

  def open_view_students_by_pass_fail_gui(self):
    self.open_student_results_gui("pass_fail")

  def open_student_results_gui(self, result_type):
    self.app.clear_window()
    self.current_page = ViewStudentResultsGUI(self.root, self.app, result_type)
    self.current_page.view_results_window()

  def open_remove_student_gui(self):
    self.app.clear_window()
    self.current_page = DeleteStudentGUI(self.root, self.app)
    self.current_page.delete_student_window()

  def clear_all_students(self):
    if not self.app.database.load_students():
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

    self.app.database.clear_students()
    messagebox.showinfo(
      "Students Cleared",
      "All student data has been cleared.",
      parent=self.root
    )

class ViewStudentGUI:
  def __init__(self, root, app):
    self.root = root
    self.app = app

  def view_student_window(self):
    title = tk.Label(
      self.root,
      text="All Students",
      **self.app.title_style
    )
    title.pack(pady=self.app.title_padding)

    students = self.app.database.load_students()

    if not students:
      empty_message = tk.Label(
        self.root,
        text="No students registered.",
        **self.app.sub_title_style
      )
      empty_message.pack(pady=self.app.sub_title_padding)
    else:
      table_frame = tk.Frame(self.root, bg=self.app.bg_color)
      table_frame.pack(fill="both", expand=True, padx=32, pady=12)

      columns = ("student_id", "name", "email")
      student_table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
      )
      student_table.heading("student_id", text="Student ID")
      student_table.heading("name", text="Name")
      student_table.heading("email", text="Email")
      student_table.column("student_id", width=140, anchor="center")
      student_table.column("name", width=220, anchor="w")
      student_table.column("email", width=360, anchor="w")

      scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=student_table.yview
      )
      student_table.configure(yscrollcommand=scrollbar.set)
      student_table.pack(side="left", fill="both", expand=True)
      scrollbar.pack(side="right", fill="y")

      for student in students:
        student_table.insert(
          "",
          "end",
          values=(student.student_id, student.name, student.email)
        )

    back_button = self.app.create_menu_button(
      self.root,
      "Back to Admin Menu",
      self.app.admin_menu,
      is_back=True
    )
    back_button.pack_configure(pady=(self.app.button_padding, 24))

class ViewStudentResultsGUI:
  grade_order = ("HD", "D", "C", "P", "Z", "No Subjects")
  result_order = ("PASS", "FAIL", "No Subjects")

  def __init__(self, root, app, result_type):
    self.root = root
    self.app = app
    self.result_type = result_type

  def view_results_window(self):
    is_grade_view = self.result_type == "grade"
    title_text = "Students by Grade" if is_grade_view else "Students by Pass/Fail"
    title = tk.Label(
      self.root,
      text=title_text,
      **self.app.title_style
    )
    title.pack(pady=self.app.title_padding)

    students = self.app.database.load_students()
    if not students:
      empty_message = tk.Label(
        self.root,
        text="No students registered.",
        **self.app.sub_title_style
      )
      empty_message.pack(pady=self.app.sub_title_padding)
    else:
      order = self.grade_order if is_grade_view else self.result_order
      grouped_students = {category: [] for category in order}

      for student in students:
        average_mark = self.get_average_mark(student.subjects)
        if average_mark is None:
          category = "No Subjects"
        elif is_grade_view:
          category = self.get_grade(average_mark)
        else:
          category = "PASS" if average_mark >= 50 else "FAIL"

        grouped_students[category].append((student, average_mark))

      table_frame = tk.Frame(self.root, bg=self.app.bg_color)
      table_frame.pack(fill="both", expand=True, padx=32, pady=12)

      columns = ("category", "student_id", "name", "average_mark")
      student_table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
      )
      student_table.heading("category", text="Grade" if is_grade_view else "Result")
      student_table.heading("student_id", text="Student ID")
      student_table.heading("name", text="Name")
      student_table.heading("average_mark", text="Average Mark")
      student_table.column("category", width=120, anchor="center")
      student_table.column("student_id", width=140, anchor="center")
      student_table.column("name", width=220, anchor="w")
      student_table.column("average_mark", width=150, anchor="center")

      scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=student_table.yview
      )
      student_table.configure(yscrollcommand=scrollbar.set)
      student_table.pack(side="left", fill="both", expand=True)
      scrollbar.pack(side="right", fill="y")

      for category in order:
        for student, average_mark in grouped_students[category]:
          average_text = f"{average_mark:.2f}" if average_mark is not None else "—"
          student_table.insert(
            "",
            "end",
            values=(category, student.student_id, student.name, average_text)
          )

    back_button = self.app.create_menu_button(
      self.root,
      "Back to Admin Menu",
      self.app.admin_menu,
      is_back=True
    )
    back_button.pack_configure(pady=(self.app.button_padding, 24))

  @staticmethod
  def get_average_mark(subjects):
    if not subjects:
      return None
    return sum(subject["mark"] for subject in subjects) / len(subjects)

  @staticmethod
  def get_grade(mark):
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

  def delete_student_window(self):
    title = tk.Label(
      self.root,
      text="Remove Student",
      **self.app.title_style
    )
    title.pack(pady=self.app.title_padding)

    prompt = tk.Label(
      self.root,
      text="Enter the 6-digit student ID to remove.",
      **self.app.sub_title_style
    )
    prompt.pack(pady=self.app.sub_title_padding)

    validate_command = (self.root.register(self.validate_student_id_input), "%P")
    self.student_id_entry = tk.Entry(
      self.root,
      validate="key",
      validatecommand=validate_command,
      **self.app.form_entry_style
    )
    self.student_id_entry.pack(pady=(0, 12))

    # validation label for invalid student ID input under the input field
    self.student_id_validation_message = tk.Label(
      self.root,
      text="",
      font=self.app.message_font,
      bg=self.app.bg_color,
      fg="#F87171"
    )
    self.student_id_validation_message.pack(pady=(0, 8))

    self.app.create_form_button(
      self.root,
      "Remove Student",
      self.remove_student
    )
    self.app.create_form_button(
      self.root,
      "Back to Admin Menu",
      self.app.admin_menu,
      is_back=True
    )

  # validate student ID input
  # number only, max length 6
  def validate_student_id_input(self, proposed_value):
    if not proposed_value:
      self.student_id_validation_message.config(text="")
      return True

    if not proposed_value.isascii() or not proposed_value.isdigit():
      self.student_id_validation_message.config(text="Numbers only.")
      return False

    if len(proposed_value) > 6:
      self.student_id_validation_message.config(text="Student ID must be at most 6 digits.")
      return False

    self.student_id_validation_message.config(text="")
    return True

  def remove_student(self):
    student_id = self.student_id_entry.get().strip()
    if not is_valid_student_id(student_id):
      messagebox.showerror(
        "Invalid Student ID",
        "Please enter a 6-digit ID.",
        parent=self.root
      )
      return

    student = self.app.database.get_student(student_id)
    if student is None:
      messagebox.showerror(
        "Student Not Found",
        f"No student found with ID {student_id}.",
        parent=self.root
      )
      return

    confirmed = messagebox.askyesno(
      "Confirm Deletion",
      f"Are you sure you want to delete {student.name} "
      f"({student.student_id})?",
      parent=self.root
    )
    if not confirmed:
      return

    if not self.app.database.delete_student(student.student_id):
      messagebox.showerror(
        "Deletion Failed",
        f"Student with ID {student.student_id} could not be found.",
        parent=self.root
      )
      return

    messagebox.showinfo(
      "Student Deleted",
      f"Student {student.name} ({student.student_id}) has been deleted.",
      parent=self.root
    )
    self.app.admin_menu()
