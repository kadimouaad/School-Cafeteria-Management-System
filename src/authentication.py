from typing import Tuple, List

import mysql
import mysql.connector
from src.dto.employee import Employee




class Authenticator:
    def __init__(self, args: dict):
        self.connection = mysql.connector.connect(
            host=args['host'],
            user=args['user'],
            password=args['password'],
            database=args['database']
        )

    def authenticate(self, entered_username,entered_password):
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




x = Authenticator({
    'host': "localhost",
    'user': "root",
    'password': "root",
    'database': "mydatabase"
})

print(x.authenticate("p","g"))