import datetime
from dao.student_dao import StudentDao
import mysql.connector
from src.dto.student import Student


student_dao = StudentDao({
    'host': "localhost",
    'user': "root",
    'password': "root",
    'database': "mydatabase"
})

print(student_dao.get_student(3))




