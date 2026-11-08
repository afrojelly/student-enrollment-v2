class Student:
    def __init__(self, name, email, password, student_id, subjects=None):
        self.name = name
        self.email = email
        self.password = password
        self.student_id = student_id
        self.subjects = subjects if subjects is not None else []

    # Automatically calculate the average mark of the student based on their subjects 
    @property
    def average_mark(self):
        if not self.subjects:
            return None

        return round(
            sum(subject["mark"] for subject in self.subjects) / len(self.subjects),
            2,
        )

    def to_record(self):
        return {
            "name":self.name, 
            "email": self.email, 
            "password":self.password, 
            "student_id": self.student_id,
            "subjects": self.subjects,
            "average_mark": self.average_mark,
        }

    #JSON, Dictionary -> student, object converting. Bring the value from the Recorded value. => allowing comparison 
    @classmethod
    def from_record(cls, record):
        return cls (
            name=record["name"],
            email=record["email"], 
            password=record["password"],
            student_id=record["student_id"],
            subjects=record.get("subjects",[]),
        )