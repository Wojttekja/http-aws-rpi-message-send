import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

import boto3
import botostubs

class LightGrid (GridLayout):
    def btn (self):
        with open ("Android_App/mode.txt", "r") as file:
            actual = file.read()
        with open ("Android_App/mode.txt", "w") as file:
            if (actual == "True"):
                file.write("False")
            else:
                file.write("True")
        s3 = boto3.resource('s3')
        s3.Object("light-control-app", "mode.txt").upload_file("Android_App/mode.txt")


class LightApp (App):
    def build(self):
        return LightGrid()


LightApp().run()