from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.material_resources import dp
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screenmanager import MDScreenManager

from src.dao.employee_dao import EmployeeDao
from src.dao.student_dao import StudentDao
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from datetime import datetime, time
import time
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.app import MDApp

from src.dto.employee import Employee
from src.dto.student import Student

Window.size = (1280, 720)

student_dao = StudentDao({
    'host': "localhost",
    'user': "root",
    'password': "root",
    'database': "mydatabase"
})

employee_dao = EmployeeDao({
    'host': "localhost",
    'user': "root",
    'password': "root",
    'database': "mydatabase"
})


def mealtype():
    x = time.localtime()
    if 6.30 <= x.tm_hour <= 7.15:
        return "breakfast"

    if 11 <= x.tm_hour <= 13:
        return "lunch"

    if 18.30 <= x.tm_hour <= 20:
        return "Dinner"
    else:
        return "closed"


class Content(BoxLayout):
    pass


class Students(MDScreen):

    def __init__(self, **kwargs):
        super(Students, self).__init__(**kwargs)

        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.6, 'center_x': 0.36},
            size_hint=(0.75, 0.6),
            use_pagination=True,
            check=True,
            column_data=[
                ("name", dp(30)),
                ("student class", dp(30)),
                ("student type", dp(30)),
                ("birthday", dp(30)),

            ],
            row_data=map(StudentDao.map_sql, student_dao.get_students(1000, 0)), )
        self.add_widget(self.data_tables)

    def add_row(self) -> None:
        name = self.ids.name.text
        student_class = self.ids.sclass.text
        student_type = self.ids.stype.text
        birthday = self.ids.birthday.text

        try:
            student_dao.add_student(Student(1, name, student_class, student_type, int(birthday)))
        except:
            pass

        self.data_tables.row_data = map(StudentDao.map_sql, student_dao.get_students(1000, 0))

    def remove_row(self) -> None:
        for i in range(1000):
            student_dao.delete_student(i)
        print("pssss")


class Stats(MDScreen):
    def __init__(self, **kwargs):
        super(Stats, self).__init__(**kwargs)

        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.6, 'center_x': 0.36},
            size_hint=(0.75, 0.6),
            use_pagination=True,
            check=True,
            column_data=[
                ("name", dp(30)),
                ("employee statue", dp(30)),
                ("birthday", dp(30)),

            ],
            row_data=map(EmployeeDao.map_sql, employee_dao.get_employees(1000, 0)), )
        self.add_widget(self.data_tables)



    def add_row(self) -> None:
        name_employee = self.ids.empname.text
        employee_statue = self.ids.empstatue.text
        empbirthday = self.ids.empbirthday.text
        try:
            employee_dao.add_employee(Employee(1, name_employee, employee_statue, int(empbirthday)))
        except:
            pass

        self.data_tables.row_data = map(EmployeeDao.map_sql, employee_dao.get_employees(1000, 0))

    def remove_row(self) -> None:
        for i in range(1000):
            employee_dao.delete_employee(i)



class MainScreen(MDScreen):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        # This now prints 1
        print(f'There are {len(self.ids.items())} id(s)')
        self.screens = [Students(), Stats()]

    def change_screen(self):
        if self.ids.student_list.state == "down":
            self.ids.main_window.switch_to(self.screens[0])
        else:
            self.ids.main_window.switch_to(self.screens[1])


class Canteen_manager(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        sm = MDScreenManager()
        root = Builder.load_file("views/MyApp.kv")
        sm.add_widget(MainScreen())
        return sm

Canteen_manager().run()
