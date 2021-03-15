from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json, glob
from datetime import datetime
from pathlib import Path
import random
#import pytz

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
    
    def login(self, username, password):
        with open("users.json") as file:
            users = json.load(file)

        if username in users and users[username]['password'] == password:
            self.manager.current = "login_screen_success"
        else:
            self.login_wrong.text = "Wrong username or password. Please try again!"



class SignUpScreen(Screen):
    def add_user(self, username, country, password, contact):  #IT CAN BE DIFFERENT FROM THOSE PARAMETERS/ID IN .KV FILE
        with open("users.json") as file:
            users = json.load(file)

        print(users)

        users[username] = {'username':username, 'password':password,'country':country, 'contact':contact}
        
        with open("users.json", "w") as file:
            json.dump(users, file)

        self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt")

        available_feelings = [Path(filename).stem for filename in available_feelings]
        
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt",'r', errors='ignore') as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"
            

class RootWidget(ScreenManager):
    pass

class ImageButton(ButtonBehavior, HoverBehavior, Image):  #hols behavior of all three items
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()