from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.lang import Builder


class LoginScreen(MDApp):

    Window.size = (460, 860)

    def build(self):
        pass

    def recuperar_senha(self):
        print("Recuperar Senha")

    def fazer_login(self):
        print("Fazer Login")

LoginScreen().run()