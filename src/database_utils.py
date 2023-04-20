import mysql.connector
from mysql.connector.errors import Error

class DatabaseController:
    def __init__(self, args: dict):
        self.connection = mysql.connector.connect(
            host=args['host'],
            user=args['user'],
            password=args['password'],
            database=args['database']
        )

    def delete_table(self, name):
        query = f'DROP TABLE {name}'
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                print(f"A table called '{name}' was deleted successfully")
        except mysql.connector.errors.ProgrammingError:
            print("Please enter a correct table name!")

    def add_table(self, name):

        query = f'CREATE TABLE {name} (id INTEGER  AUTO_INCREMENT, name VARCHAR(255),  student_class VARCHAR(255), student_type VARCHAR(255), birth_date INTEGER(10), PRIMARY KEY (id))'
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                print(f"A table called '{name}' was added successfully")
        except mysql.connector.errors.ProgrammingError:
            print("Wrong name.. Please try again")

    def add_employee_table(self, name):

        query = f'CREATE TABLE {name} (id INTEGER  AUTO_INCREMENT, name VARCHAR(255),  employee_statue VARCHAR(255), birth_date INTEGER(10), PRIMARY KEY (id))'
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                print(f"A table called '{name}' was added successfully")
        except mysql.connector.errors.ProgrammingError:
            print("Wrong name.. Please try again")
