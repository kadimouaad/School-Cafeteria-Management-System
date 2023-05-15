class Employee:
    def __init__(self, id, name, employee_statue, birth_date):
        self.employee_statue = employee_statue
        self.name = name
        self.birth_date = birth_date


    def __str__(self) -> str:
        return f"Name: {self.name}\n" \
               f"employee_statue: {self.employee_statue}\n"\
               f"Birth_date: {self.birth_date}\n" \
