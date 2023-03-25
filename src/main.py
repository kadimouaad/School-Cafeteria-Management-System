from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivymd.app import MDApp

from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

Window.size = (1280, 720)

Builder.load_file("views/MyApp.kv")


class MDScreen(Screen):
    pass


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return MDScreen()


Example().run()
