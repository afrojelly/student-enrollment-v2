import re

def is_valid_student_id(student_id):
    return re.fullmatch(r"[0-9]{6}", student_id) is not None

# def initialize(): 

# def read_from_file():

# def write_to_file(customers): 


def validate_email(email): #email  #  actioned. Todo: email format: firstname.lastname@university.com  # 현재 특수문자 입력이 허용돼서 아이디 부분 "문자.문자" 형식만 입력 가능하도록 validation 수정 => actioned!
    pattern = r"[A-Za-z]+\.[A-Za-z]+@university\.com"
    return bool(re.fullmatch(pattern, email))
#currently register multiple accounts with the same email address. Since we only have  pattern validation right now, should i add a duplicate email check before completing the registration ?  


def validate_password(password): #password  #  actioned. Todo: password format이 현재는 대문자 + 영문4글자 + 숫자3자리로 고정되어있는데, 대문자 시작 부분만 고정하고 뒤에는 영문, 숫자 입력 순서 상관없이 가능하도록 수정 필요 => actioned!
    # pattern = r"[A-Z][A-Za-z0-9]*"
    pattern = r"[A-Z][A-Za-z]{4,}[0-9]{3,}"
    return bool(re.fullmatch(pattern, password)
    )

def go_back(prompt):
    value = input(prompt)
    if value.lower() == "x":
        print("Returning to the previous menu.")
        return None
    return value

