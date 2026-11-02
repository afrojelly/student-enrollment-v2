class Student:
    def __init__(self, name, email, password, studentId, subjects=None):
        self.name = name
        self.email = email
        self.password = password
        self.studentId = studentId
        self.subjects = subjects if subjects is not None else []

    def toRecord(self):
        return {
            "name":self.name, 
            "email": self.email, 
            "password":self.password, 
            "studentId": self.studentId, 
            "subjects": self.subjects,   
         }


#Jason, Dictionary -> student, object converting. Bring the value from the Recorded value. => allowing comparison 
    @classmethod
    def fromRecord(cls, record):
        return cls (
            name=record["name"],
            email=record["email"], 
            password=record["password"],
            studentId=record["studentId"],
            subjects=record.get("subjects",[]),
        )

