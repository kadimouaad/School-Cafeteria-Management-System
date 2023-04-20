from typing import List, Tuple
from src.dto.employee import Employee
import mysql.connector
from mysql.connector.errors import Error


class Employee_Dao:
    def __init__(self, args: dict):
        self.connection = mysql.connector.connect(
            host=args['host'],
            user=args['user'],
            password=args['password'],
            database=args['database']
        )
    def get_employee(self, id: int) -> Employee:
        with self.connection.cursor() as cursor:
            cursor.execute(f'SELECT * FROM Employee_list WHERE id = {id}')
            for employee in cursor.fetchall():
                return self._map(employee)

    def get_employees(self, limit, skip) -> List[Employee]:
        r = []
        with self.connection.cursor() as cursor:
            cursor.execute(f'SELECT * FROM Employee_list LIMIT {skip}, {limit}')
            for emp in cursor.fetchall():
                r.append(str(self._map(emp)))
        return r

    def add_employee(self, employee: Employee):
        query = """
        INSERT INTO Employee_list
        (name, employee_statue, birth_date)
        VALUES ( %s, %s, %s )
        """
        with self.connection.cursor() as cursor:
            cursor.executemany(query, self._map_sql(employee))
            self.connection.commit()

    def delete_employee(self, id: int) -> Employee:
        query = f'Delete from Employee_list where id = {id}'
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()

    def update_employee(self, employee: Employee,id):
        query = f"UPDATE Employee_list SET name=%s, employee_statue=%s, birth_date=%s WHERE id={id}"


        with self.connection.cursor() as cursor:
            cursor.executemany(query, self._map_sql(employee))
            self.connection.commit()

    def authenticate(self, entered_username,):
        query = f"SELECT * FROM employee_user WHERE username = %s "

        with self.connection.cursor() as cursor:
            cursor.execute(query,entered_username)

    @staticmethod
    def _map(employee_dic: dict) -> Employee:
        return Employee(employee_dic[0],
                        employee_dic[1],
                        employee_dic[2],
                        employee_dic[3]
                        )

    @staticmethod
    def _map_sql(employee: Employee) -> List[Tuple]:
        return [
            (employee.name, employee.employee_statue, employee.birth_date)]
