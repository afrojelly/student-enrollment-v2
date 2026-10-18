import tkinter as tk
from tkinter import messagebox

from cli.student_registration import validatePassword
from cli.change_password import verifyPassword,updatePassword

class changePasswordGUI:

    def __init__(self,root,app,student):
        self.root = root
        self.app = app
        self.student = student 

#1. change PAssword Window 생성 
    def changePasswordWindow(self):
        self.app.clearWindow()
        self.passwordTitle = tk.Label(
            self.root,
            text = "would you like to change your password?",
            **self.app.titleStyle
        )
        self.passwordTitle.pack (pady=self.app.titlePadding)

        self.passwordSubtitle = tk.Label(
            self.root,
            text = f"Please verify your current password, {self.student.name}",
            **self.app.subTitleStyle
        )
        self.passwordSubtitle.pack(
            pady=self.app.subTitlePadding
        )

#current Password validation (page 1)
        self.currentPasswordLabel= tk.Label(
            self.root,
            text="current Password",
            **self.app.formLabelStyle
        )
        self.currentPasswordLabel.pack(pady = (5,5))

        self.currentPasswordEntry = tk.Entry(
            self.root,
            **self.app.formEntryStyle,
            show ="*" #비밀번호가 보이지 않게함, 이거 지우면 password 볼 수 있음 참고
        )
        self.currentPasswordEntry.pack(pady=(0,10))


        self.verifyButton = self.app.createFormButton(
            self.root,
            "Verify",
            self.verifyCurrentPassword
        )

        # Back Button
        self.exitButton = self.app.createFormButton(
            self.root,
            "Exit",
            self.exitChangePassword,
            isBack=True
        )
#2. trtun to subject enrolment page  
    def exitChangePassword(self):
        self.app.subjectEnrolmentPage(self.student)

#3. current password varity 
    def verifyCurrentPassword(self):
        currentPassword = self.currentPasswordEntry.get()

        if not verifyPassword(self.student, currentPassword):
            messagebox.showerror(
                "Verification Failed",
                "Current password is incorrect. Please try again."
            )
            return
        
        else: 
            messagebox.showinfo(
                "Verification Successful",
                "Current password verified successfully!"
            )
            self.newPassword()
#=> once validate the current password, it will go to the next new page, enter new password 
 #4. once matched the current password, can go change the password    
    def newPassword(self):
        self. app.clearWindow()

        self.newPasswordTitle = tk.Label(
            self.root,
            text = "Plase Enter your New Password",
            **self.app.subTitleStyle
        )
        self.newPasswordTitle.pack(
            pady = self.app.titlePadding
        )
        # New Password Label
        self.newPasswordLabel = tk.Label(
            self.root,
            text="New Password",
            **self.app.formLabelStyle
        )
        self.newPasswordLabel.pack(pady=(5, 5))

        # New Password Entry
        self.newPasswordEntry = tk.Entry(
            self.root,
            **self.app.formEntryStyle,
            show="*"
        )
        self.newPasswordEntry.pack(pady=(0, 5))

        # Password Hint
        self.passwordHint = tk.Label(
            self.root,
            text="Uppercase first | At least 5 letters | At least 3 digits",
            **self.app.hintStyle
        )
        self.passwordHint.pack(pady=(0, 10))

        # Confirm Password Label
        self.confirmPasswordLabel = tk.Label(
            self.root,
            text="Confirm New Password",
            **self.app.formLabelStyle
        )
        self.confirmPasswordLabel.pack(pady=(5, 5))

        # Confirm Password Entry
        self.confirmPasswordEntry = tk.Entry(
            self.root,
            **self.app.formEntryStyle,
            show="*"
        )
        self.confirmPasswordEntry.pack(pady=(0, 15))

        # Confirm Button
        self.confirmButton = self.app.createFormButton(
            self.root,
            "Confirm",
            self.saveNewPassword
        )

        # Exit Button
        self.exitButton = self.app.createFormButton(
            self.root,
            "Exit",
            self.exitChangePassword,
            isBack=True
        )
#saved new Passwordd 
    def saveNewPassword(self):
        newPassword = self.newPasswordEntry.get()
        confirmPassword = self.confirmPasswordEntry.get()

        result = updatePassword(
            self.student,
            self.app.students,
            self.app.database,
            newPassword,
            confirmPassword
        )

        if result == "success":
            messagebox.showinfo(
                "Password Changed Successfully",
                "Please use your new password the next time you log in!"
            )
            self.exitChangePassword()

        else:
            if result == "invalid":
                messagebox.showerror(
                    "Invalid Password",
                    "Password must start with an uppercase letter,\n"
                    "contain at least 5 letters and at least 3 digits."
                )

            elif result == "mismatch":
                messagebox.showerror(
                    "Password Mismatch",
                    "Passwords do not match. Please try again."
                )

            elif result == "saveError":
                messagebox.showerror(
                    "Database Error",
                    "Unable to save the new password."
                )

            else:
                messagebox.showerror(
                    "Change Password Failed",
                    "Unable to update your password."
                )
