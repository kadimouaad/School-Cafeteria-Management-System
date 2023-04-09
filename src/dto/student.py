class Student:
    def __init__(self, id, name, student_class, student_type, birth_date):
        self.student_type = student_type
        self.student_class = student_class
        self.name = name
        self.birth_date = birth_date

    def __str__(self) -> str:
        return f"Name: {self.name}\n" \
               f"student_class: {self.student_class}\n" \
               f"student_type: {self.student_type}\n"\
               f"Birth_date: {self.birth_date}\n" \


