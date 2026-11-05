class Student:
    def __init__(self, name, email, password, student_id, subjects=None):
        self.name = name
        self.email = email
        self.password = password
        self.student_id = student_id
        self.subjects = subjects if subjects is not None else []
        #self.recalculate_average()  # Calculate average mark upon initialization vs calculating it on demand

    def to_record(self):
        return {
            "name":self.name, 
            "email": self.email, 
            "password":self.password, 
            "studentId": self.student_id,
            "subjects": self.subjects,   
        }


#Jason, Dictionary -> student, object converting. Bring the value from the Recorded value. => allowing comparison 
    @classmethod
    def from_record(cls, record):
        return cls (
            name=record["name"],
            email=record["email"], 
            password=record["password"],
            student_id=record["studentId"],
            subjects=record.get("subjects",[]),
        )

