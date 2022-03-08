from tokenize import String

import kivy
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from numpy import source
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


import random
import datetime
from calendar import month
from time import time
from PIL import Image, ImageFont, ImageDraw


tech = 0

KV = """
WindowManager:
    MyBl:
    ThirdWindow:
    SecondWindow:

<MyBl>:
    numb: numb_inp.text
    rou: rou_inp.text
    
    BoxLayout:
        name: "first"

        orientation: "vertical"
        
        padding: 20
        spacing: 10
        
        Label:
            font_size: "30sp"
            text: root.data_label
        
        TextInput:
            id: numb_inp
            multiline: False
            padding_y: (5,5)
            size_hint: (1, 0.5)
            
        Label:
            font_size: "30sp"
            text: root.data_label2
        
        TextInput:
            id: rou_inp
            multiline: False
            padding_y: (5,5)
            size_hint: (1, 0.5)
        
        Label:
            font_size: "30sp"
            text: root.data_label3      
                
        Button:
            text: "Трл / Авт"
            bold: True
            background_color: '#00FFCE'
            size_hint: (1,0.5)
            on_press: root.tech_change()  
            
        Button:
            text: "Продолжить"
            bold: True
            background_color: '#00FFCE'
            size_hint: (1,0.5)
            on_press: root.callback() 
            on_press: app.root.current = "third"          

<SecondWindow>:
    name: "second"
    
    BoxLayout:
        orientation: "vertical"
        
        Image: 
            source: 'ticket.png'
            
<ThirdWindow>:
    name: "third"
    
    BoxLayout:
        orientation: "vertical"
        
        Button:
            text: "Продолжить"
            bold: True
            background_color: '#00FFCE'
            size_hint: (1,0.5)
            on_press: app.root.current = "second"
                    
"""


class WindowManager(ScreenManager):
    pass


class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass


class MyBl(Screen):

    def __init__(self, **kwargs):

        super(MyBl, self).__init__(**kwargs)

    data_label = StringProperty("Рег номер :")
    data_label2 = StringProperty("Маршрут :")
    data_label3 = StringProperty("Автобус")
    numb = StringProperty()
    rou = StringProperty()
    typet = "A"
    
    def callback(self):
        print(self.numb, " ", self.rou, " ", self.typet)
        img = Image.open('as.png')
        Idraw = ImageDraw.Draw(img)

        dt = datetime.datetime.now()

        day = ""
        month = ""
        year = ""
        hour = ""
        minute = ""
        second = ""

        if len(str(dt.day)) < 2:
            day = "0" + str(dt.day)
        else:
            day = str(dt.day)

        if len(str(dt.month)) < 2:
            month = "0" + str(dt.month)
        else:
            month = str(dt.month)

        if len(str(dt.year)) < 2:
            year = "0" + str(dt.year)
        else:
            year = str(dt.year)
        #############################
        #############################
        #############################
        date = day + "." + month + "." + year

        #############################
        #############################
        #############################

        if len(str(dt.hour)) < 2:
            hour = "0" + str(dt.hour)
        else:
            hour = str(dt.hour)
        if len(str(dt.minute)) < 2:
            minute = "0" + str(dt.minute)
        else:
            minute = str(dt.minute)
        if len(str(dt.second)) < 2:
            second = "0" + str(dt.second)
        else:
            second = str(dt.second)

        time = hour + ":" + minute + ":" + second

        #############################
        #############################
        #############################
        stations = {"124": [""""Лошица-2" """, """- Ст Пушкинская"""]}

        headline = ImageFont.truetype('arial.ttf', size=55)
        headline1 = ImageFont.truetype('arial.ttf', size=47)
        headline2 = ImageFont.truetype('arial.ttf', size=35)

        #tech_type = input("А - Автобус / T - Троллейбус ")
        #reg_num = input("Рег номер ")
        #route = input("Маршрут ")

        tech_type = self.typet
        reg_num = self.numb
        route = self.rou

        route_stations1 = ""
        route_stations2 = ""

        if str(route) in stations:
            route_stations1 = stations[route][0]
            route_stations2 = stations[route][1]
        else:
            route_stations1 = """ДС - "156" """
            route_stations2 = """ - ДС "12K" """

        Idraw.text(
            (512, 1735), f"""{reg_num} {tech_type}_№{route} ({route_stations1}""", font=headline1, fill='#1C0606')
        Idraw.text((527, 1800), f"""{route_stations2}).""",
                   font=headline1, fill='#1C0606')

        tech_number = random.randint(1234, 9765)
        ticket_number = random.randint(101342, 978543)

        Idraw.text((1035, 45), f"{hour}:{minute}", font=headline2)
        Idraw.text((216, 1960), f"010{tech_number}",
                   font=headline, fill='#1C0606')
        Idraw.text(
            (714, 1960), f"ES007{ticket_number}", font=headline, fill='#1C0606')
        Idraw.text((216, 2150), f"{date}", font=headline, fill='#1C0606')
        Idraw.text((847, 2150), f"{time}", font=headline, fill='#1C0606')

        draw = ImageDraw.Draw(img)
        draw.line((216, 2014, 435, 2014), fill=15, width=4)

        img.save('ticket.png')

    def tech_change(self):
        global tech
        tech += 1
        if tech % 2 == 0:
            self.data_label3 = "Автобус"
            self.typet = "A"
        if tech % 2 != 0:
            self.data_label3 = "Троллейбус"
            self.typet = "T"


class MyApp(App):

    running = True

    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self.running = False


MyApp().run()
