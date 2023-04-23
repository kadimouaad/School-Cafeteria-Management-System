from typing import Tuple, List

import mysql
import mysql.connector
from src.dto.employee import Employee
from src.dao.employee_dao import EmployeeDao




class Authenticator:
    def __init__(self, args: dict):
        self.connection = mysql.connector.connect(
            host=args['host'],
            user=args['user'],
            password=args['password'],
            database=args['database']
        )

    def authenticate_login(self, entered_username,entered_password):
        query = f"SELECT * FROM employee_user WHERE username = %s AND password = %s"

        with self.connection.cursor() as cursor:
            cursor.execute(query,(entered_username,entered_password))
            a = cursor.fetchall()
            return a

    def register(self,username,password):   #  register a new user employee
        query ="""
        INSERT INTO Employee_user
        (username, password)
        VALUES ( %s, %s)
        """

        with self.connection.cursor() as cursor:
            cursor.execute(query,(username,password))
            self.connection.commit()

    def authentificate_student(self,info):
        student_info = EmployeeDao({
             'host': "localhost",
             'user': "root",
             'password': "root",
             'database': "mydatabase"
        })
        x = student_info.get_employee(info)
        if x[0] == '1':
            print("hhohoh")
        else:
            print("siuu")
        return x






x = Authenticator({
    'host': "localhost",
    'user': "root",
    'password': "root",
    'database': "mydatabase"
})
print(x.authentificate_student(1))

