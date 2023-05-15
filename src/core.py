import datetime
import cv2.cv2
from dao.student_dao import StudentDao
import mysql.connector
from src.dto.student import Student
from src.database_utils import DatabaseController
from src.dao.employee_dao import EmployeeDao
from src.dto.employee import Employee
from src.qrscanner import Scanner
import cv2
import webbrowser
from datetime import datetime
import time


student_dao = EmployeeDao({
    'host': "localhost",
    'user': "root",
    'password': "root",
    'database': "mydatabase"
})







