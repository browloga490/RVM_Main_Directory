#!/usr/bin/python3.6
import kivy
kivy.require("1.0.9")
import os
import csv
import time

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.progressbar import ProgressBar
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from kivy.graphics.context_instructions import Color
from kivy.clock import Clock

from kivy.config import Config
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')
Config.write()
#Window.size = (1024, 600)

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class Channel_1(Widget):
    pass

class Channel_2(ScreenManager):
    pass

class Channel_3(ScreenManager):
    pass

class Channel_4(ScreenManager):
    pass

class CalcGridLayout(GridLayout):
    pass

class OptGridLayout(GridLayout):
    pass

class Label(Label):

     def update(self, nv):
        self.text = nv

class CustomPopup(Popup):
    pass

        
    
class Graph_Tabs(TabbedPanel):

    do_default_tab = False
    tab_pos = 'top_mid'
    tab_width = Window.width / 5

class Channel_Tabs(TabbedPanel):

    do_default_tab = False
    tab_pos = 'top_mid'
    tab_width = Window.width / 4

    ch1_val = StringProperty()
    ch2_val = StringProperty()
    ch3_val = StringProperty()
    ch4_val = StringProperty()

    ch1_rating = StringProperty()
    ch2_rating = StringProperty()
    ch3_rating = StringProperty()
    ch4_rating = StringProperty()

    ch1_color = ObjectProperty()
    ch2_color = ObjectProperty()
    ch3_color = ObjectProperty()
    ch4_color = ObjectProperty()

    current_val = NumericProperty(0)

    pb = ObjectProperty()

    def __init__(self, **kwargs):
        super(Channel_Tabs, self).__init__(**kwargs)
        self.ch1_val = str(0)
        self.ch2_val = str(0)
        self.ch3_val = str(0)
        self.ch4_val = str(0)

        self.ch1_rating = "NOT CONNECTED"
        self.ch2_rating = "NOT CONNECTED"
        self.ch3_rating = "NOT CONNECTED"
        self.ch4_rating = "NOT CONNECTED"

        self.ch1_color = (0,0,1,1)
        self.ch2_color = (0,0,1,1)
        self.ch3_color = (0,0,1,1)
        self.ch4_color = (0,0,1,1)

        self.pb = ProgressBar()
        self.popupk = Popup(title='Performing Quick Read...', title_size=30,
                            title_align='center', size_hint=(0.40,0.15),
                            auto_dismiss=False,separator_height=0)#content=self.pb)
        
        
        self.current_val = 0

    def prog_bar_start(self):
        self.pb.min = 0
        self.pb.max = 60
        self.pb.value = 0
        self.popupk.open()

        Clock.schedule_once(self.read,0)
        Clock.schedule_once(self.write,0)
        Clock.schedule_once(self.show,0)

    def update(self, *args):
        self.pb.value = 30#self.current_val

    def read(self, *args):
        #os.system(r"/usr/local/natinst/nidaqmxbase/examples/ai/./quickRead_2048_4Ch")
        self.pb.value = 20
        print(self.pb.value)

    def write(self, *args):
        os.chdir(r"/usr/local/RVMD/LabView_Execs/Rev_1/LabCh0/My Shared Library 2/")
        os.system("./read")
        self.pb.value = 40
        print(self.pb.value)

    def show(self, *args):
 
        os.chdir(r"/usr/local/RVMD/GUI/")
		
        file = open('quick_mem.txt', 'r')
        csv_reader = csv.reader(file)
        init_val = next(csv_reader)
        print(init_val)

        self.ch1_val = str(init_val[0])
        self.ch2_val = str(init_val[1])
        self.ch3_val = str(init_val[2])
        self.ch4_val = str(init_val[3])
        self.pb.value = 60

        if init_val[0] == "NaN":
            self.ch1_rating = "NOT CONNECTED"
            self.ch1_color = (0,0,1,1)
        elif float(init_val[0]) < 0:
            self.ch1_rating = "NOT CONNECTED"
            self.ch1_color = (0,0,1,1)
        elif float(init_val[0]) <= 0.07:
            self.ch1_rating = "GOOD"
            self.ch1_color = (0,1,0,1)
        elif float(init_val[0]) > 0.07 and float(init_val[0]) <= 0.18:
            self.ch1_rating = "SATISFACTORY"
            self.ch1_color = (1,1,0,1)
        elif float(init_val[0]) > 0.18 and float(init_val[0]) <= 0.44:
            self.ch1_rating = "UNSATISFACTORY"
            self.ch1_color = (1,0.65,0,1)
        elif float(init_val[0]) > 0.44:
            self.ch1_rating = "UNACCEPTABLE"
            self.ch1_color = (1,0,0,1)

        if init_val[1] == "NaN":
            self.ch2_rating = "NOT CONNECTED"
            self.ch2_color = (0,0,1,1)
        elif float(init_val[1]) < 0:
            self.ch1_rating = "NOT CONNECTED"
            self.ch1_color = (0,0,1,1)
        elif float(init_val[1]) <= 0.07:
            self.ch2_rating = "GOOD"
            self.ch2_color = (0,1,0,1)
        elif float(init_val[1]) > 0.07 and float(init_val[1]) <= 0.18:
            self.ch2_rating = "SATISFACTORY"
            self.ch2_color = (1,1,0,1)
        elif float(init_val[1]) > 0.18 and float(init_val[1]) <= 0.44:
            self.ch2_rating = "UNSATISFACTORY"
            self.ch2_color = (1,0.65,0,1)
        elif float(init_val[1]) > 0.44:
            self.ch2_rating = "UNACCEPTABLE"
            self.ch2_color = (1,0,0,1)

        if init_val[2] == "NaN":
            self.ch3_rating = "NOT CONNECTED"
            self.ch3_color = (0,0,1,1)
        elif float(init_val[2]) < 0:
            self.ch1_rating = "NOT CONNECTED"
            self.ch1_color = (0,0,1,1)
        elif float(init_val[2]) <= 0.07:
            self.ch3_rating = "GOOD"
            self.ch3_color = (0,1,0,1)
        elif float(init_val[2]) > 0.07 and float(init_val[2]) <= 0.18:
            self.ch3_rating = "SATISFACTORY"
            self.ch3_color = (1,1,0,1)
        elif float(init_val[2]) > 0.18 and float(init_val[2]) <= 0.44:
            self.ch3_rating = "UNSATISFACTORY"
            self.ch3_color = (1,0.65,0,1)
        elif float(init_val[2]) > 0.44:
            self.ch3_rating = "UNACCEPTABLE"
            self.ch3_color = (1,0,0,1)

        if init_val[3] == "NaN":
            self.ch4_rating = "NOT CONNECTED"
            self.ch4_color = (0,0,1,1)
        elif float(init_val[3]) < 0:
            self.ch1_rating = "NOT CONNECTED"
            self.ch1_color = (0,0,1,1)
        elif float(init_val[3]) <= 0.07:
            self.ch4_rating = "GOOD"
            self.ch4_color = (0,1,0,1)
        elif float(init_val[3]) > 0.07 and float(init_val[3]) <= 0.18:
            self.ch4_rating = "SATISFACTORY"
            self.ch4_color = (1,1,0,1)
        elif float(init_val[3]) > 0.18 and float(init_val[3]) <= 0.44:
            self.ch4_rating = "UNSATISFACTORY"
            self.ch4_color = (1,0.65,0,1)
        elif float(init_val[3]) > 0.44:
            self.ch4_rating = "UNACCEPTABLE"
            self.ch4_color = (1,0,0,1)

        print(self.pb.value)
        self.popupk.dismiss()
            
    def quick_read(self, *args):
        
        os.system(r"/usr/local/natinst/nidaqmxbase/examples/ai/./quickRead_2048_4Ch")
        time.sleep(1)
        self.current_val = 10
        self.update
        Clock.schedule_once(self.update,0)
        #load_pop.open()

        os.chdir(r"/usr/local/RVMD/LabView_Execs/Rev_1/LabCh0/My Shared Library 2/")
        time.sleep(1)
        self.current_val = 20

        os.system("./read")
        time.sleep(1)
        #self.pb.value = 30
        self.current_val = 30

        os.chdir(r'/usr/local/RVMD/GUI/')
        time.sleep(1)
        #self.pb.value = 40
        self.current_val = 40

        file = open('quick_mem.txt', 'r')
        csv_reader = csv.reader(file)
        init_val = next(csv_reader)
        print(init_val)
        #self.pb.value = 50
        self.current_val = 50

        self.ch1_val = str(init_val[0])
        self.ch2_val = str(init_val[1])
        self.ch3_val = str(init_val[2])
        self.ch4_val = str(init_val[3])
        self.current_val = 60

        self.popupk.dismiss()
        
    def open_popup(self):
      
        main_frame = BoxLayout(orientation='vertical')
        top = GridLayout(rows=2,padding=10,spacing=10)
        bottom = BoxLayout()

        box_1 = BoxLayout()
        
        lbl_1 = Label(text='Channel 1',font_size=25)
        lbl_2 = Label(text='Channel 2',font_size=25)
        lbl_3 = Label(text='Channel 3',font_size=25)
        lbl_4 = Label(text='Channel 4',font_size=25)
        
        
        box_1.add_widget(lbl_1)
        box_1.add_widget(lbl_2)
        box_1.add_widget(lbl_3)
        box_1.add_widget(lbl_4)
        
        box_2 = BoxLayout()

        #USE A GRIDLAYOUT FOR THE BOX 1 & 2
        top.add_widget(box_1)
        top.add_widget(box_2)

        box_3 = BoxLayout()
        
        btn_1 = Button(text='Quick Read')
        btn_2 = Button(text='Close')
        
        box_3.add_widget(btn_1)
        box_3.add_widget(btn_2)

        bottom.add_widget(box_3)
        
        main_frame.add_widget(top)
        main_frame.add_widget(bottom)
        
        popup = Popup(title='Quick Read', title_size=30, title_align='center', content=main_frame, size_hint=(0.75,0.75), auto_dismiss=True)
        
        btn_1.bind(on_press = self.quick_read)
        btn_2.bind(on_press = popup.dismiss)

       
        popup.open()

        
#presentation = Builder.load_file("main.kv")


        
class MainApp(App):
    
    def build(self):
        return Builder.load_file("main.kv")#presentation

if __name__ == "__main__":
    MainApp().run()

