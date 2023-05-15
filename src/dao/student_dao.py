from typing import List, Tuple
from src.dto.student import Student
import mysql.connector
from mysql.connector.errors import Error


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
                return self.map(student)

    def get_students(self, limit, skip) -> List[Student]:
        r = []
        with self.connection.cursor() as cursor:
            cursor.execute(f'SELECT * FROM student_list LIMIT {skip}, {limit}')
            for student in cursor.fetchall():
                r.append(self.map(student))
        return r

    def add_student(self, student: Student):
        query = """
        INSERT INTO student_list
        (name, student_class,student_type, birth_date)
        VALUES ( %s, %s, %s, %s )
        """
        with self.connection.cursor() as cursor:
            cursor.executemany(query, (self.map_sql(student),))
            self.connection.commit()

    def delete_student(self, id: int) -> Student:
        query = f'Delete from student_list where id = {id}'
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()

    def update_student(self, student: Student,id):
        query = f"UPDATE student_list SET name=%s, student_class=%s, student_type=%s, birth_date=%s WHERE id={id}"


        with self.connection.cursor() as cursor:
            cursor.executemany(query, self.map_sql(student))
            self.connection.commit()


    @staticmethod
    def map(student_dic: dict) -> Student:
        return Student(student_dic[0],
                       student_dic[1],
                       student_dic[2],
                       student_dic[3],
                       student_dic[4]
                       )

    @staticmethod
    def map_sql(student: Student) -> Tuple:
        return student.name, student.student_class, student.student_type, student.birth_date
