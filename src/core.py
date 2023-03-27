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


student_dao.update_student("yaaaa", "GG", 2)



