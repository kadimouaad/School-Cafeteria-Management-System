import mysql.connector
from mysql.connector.errors import Error

class DatabaseController:

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
