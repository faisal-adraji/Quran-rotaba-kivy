'''
author  :   Faisal Adraji
email   :   faisal.adraji@gmail.com
version :   0.0
start   :   12-2017
kivy.require("1.9.0")
'''


#import sys
#sys.path.append("/storage/emulated/0/kivy/Tin")

# import threading
import kivy
kivy.require("1.9.0")

#necesary for utf
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from kivy.animation import Animation
from kivy.uix.scrollview import ScrollView
from kivy.metrics import sp, dp


from kivy.lang import Builder

Builder.load_string('''
<Rotaba>:


    ''')


class RotabaLabel(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(.5, .5, .5, 1)
            Rectangle(pos=self.pos, size=self.size)



class Rotaba(FloatLayout):
    
    isfirsttime = 1
    
    #ti = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Rotaba, self).__init__(**kwargs)
        
    def update(self, dt):

        #your initial update here
        if self.isfirsttime:
            self.isfirsttime = 0



    #functions for buttons

    def autoscroll(self, sv, box, autoscroll_btn):
        pass

class RotabaApp(App):

    global Window
    global wdg


    def build(self):

        Window.set_title('Quran Rotaba')
        self.title = 'Quran Rotaba'
        self.icon = 'rotaba.png'
        #self.presplash = Image(source= 'tin_splash.png', allow_stretch= False)
        self.wdg = Rotaba(size= Window.size)
        main_wdg = self.wdg


        #restore last session
        # f = open("save.dat")
        # self.curt_page = f.readline()
        # box.size_hint[1] = int(f.readline())
        # sv.spd = int(f.readline())
        # f.close()
        
        
        
        # initializing graphic objects

        Clock.schedule_interval(main_wdg.update, 1.0 / 60.0)
        return main_wdg

    def on_stop(self):
        pass
        # f = open("save.dat", "w")
        # f.write( str(curt_page -1) + '\n')  
        # f.write( str(size) + '\n')
        # f.write( str(spd) )
        # # f.write(  str((1 - SCROLL_Y/1)*604)  )  
        # f.close()



if __name__ == '__main__':
    RotabaApp().run()