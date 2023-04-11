import datetime
from dao.student_dao import StudentDao
import mysql.connector
from src.dto.student import Student
from src.database_utils import DatabaseController


student_dao = StudentDao({
    'host': "localhost",
    'user': "root",
    'password': "root",
    'database': "mydatabase"
})





