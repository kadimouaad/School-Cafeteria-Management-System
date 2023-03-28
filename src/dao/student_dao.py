from typing import List, Tuple
from src.dto.student import Student
import mysql.connector


class StudentDao:
    def __init__(self, args: dict):
        self.connection = mysql.connector.connect(
            host=args['host'],
            user=args['user'],
            password=args['password'],
            database=args['database']
        )

    def get_student(self, id: int) -> Student:
        with self.connection.cursor() as cursor:
            cursor.execute(f'SELECT * FROM student_list WHERE id = {id}')
            for student in cursor.fetchall():
                return self._map(student)

    def get_students(self, limit, skip) -> List[Student]:
        r = []
        with self.connection.cursor() as cursor:
            cursor.execute(f'SELECT * FROM student_list LIMIT {skip}, {limit}')
            for student in cursor.fetchall():
                r.append(self._map(student))
        return r

    def add_student(self, student: Student):
        query = """
        INSERT INTO student_list
        (name, student_class,student_type, birth_date)
        VALUES ( %s, %s, %s, %s )
        """
        with self.connection.cursor() as cursor:
            cursor.executemany(query, self._map_sql(student))
            self.connection.commit()

    def delete_student(self, id: int) -> Student:
        query = f'Delete from student_list where id = {id}'
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()

    def update_student(self,name:str, student:str, id:int):

        with self.connection.cursor() as cursor:
            cursor.execute(f"UPDATE student_list SET name , student_class VALUES('%s', '%s')  WHERE id = {id}", (name, student))
            self.connection.commit()


    def delete_table(self, name):
        query = f'DROP TABLE {name}'
        with self.connection.cursor() as cursor:
            cursor.execute(query)

    def add_table(self, name):

        query = f'CREATE TABLE {name} (id INTEGER  AUTO_INCREMENT, name VARCHAR(255),  student_class VARCHAR(255), student_type VARCHAR(255), birth_date INTEGER(10), PRIMARY KEY (id))'
        with self.connection.cursor() as cursor:
            cursor.execute(query)



    @staticmethod
    def _map(student_dic: dict) -> Student:
        return Student(student_dic[0],
                       student_dic[1],
                       student_dic[2],
                       student_dic[3],
                       student_dic[4]
                       )

    @staticmethod
    def _map_sql(student: Student) -> List[Tuple]:
        return [
            (student.id ,student.name, student.student_class, student.student_type, student.birth_date)]
