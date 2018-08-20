'''
author  :   Faisal Adraji
email   :   faisal.adraji@gmail.com
version :   0.0
start   :   12-2017
kivy.require("1.9.0")
'''

#ta ra rum pum
#import sys
#sys.path.append("/storage/emulated/0/kivy/Tin")

# import threading
import kivy
kivy.require("1.9.0")

#necesary for utf
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from random import randint


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
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from kivy.core.window import Window
from kivy.metrics import sp, dp
from kivy.uix.scrollview import ScrollView


from kivy.lang import Builder

Builder.load_string('''
<Rotaba>:

    ScrollView:
        id: sv
        size_hint_x: 1.0001
        size_hint_y: .9
        pos_hint: {'x':0, 'y':0}
        StackLayout:
            id: box
            size_hint: (1.001, 2)
            rows: 12
            cols: 1
            orientation: 'rl-tb'
            padding: '20dp'
            spacing: '20dp'


            AyaLabel:
                id: lbl
                size_hint_x: None
                size_hint_y: None
                background_color: 1,1,0,1

                size: self.parent.size[0],200
                # canvas:
                #     Color:
                #         rgba: 0, 1, 1, 1
                #     Rectangle:
                #         pos: self.pos[0],self.pos[1]
                #         size: self.size[0],self.size[1]
                Image:
                    color: 1,1,0,1
                    source: 'ayat_database/1_1.png'
                    pos: lbl.pos
                    #size: lbl.size
                    size: self.parent.size

            AyaButton:
                id: btn
                size_hint: None, None
                background_color: 0,3,3,1
                on_press: root.next_aya(btn,0)
                size: self.parent.size[0],200

                # size: 300,200
                # canvas:
                #     Color:
                #         rgba: 0, 1, 1, 1
                #     Rectangle:
                #         pos: self.pos[0],self.pos[1]
                #         size: self.size[0],self.size[1]
                Image:
                    color: 0,1,1,1
                    source: 'ayat_database/1_1.png'
                    pos: btn.pos
                    size: self.parent.size
                    #size: btn.size
                    #size: self.texture_size[0]/2, self.texture_size[1]/2


            AyaButton:
                id: btn2
                size_hint_x: None
                size_hint_y: None
                background_color: 0,3,3,1
                on_press: root.next_aya(btn2,1)
                size: self.parent.size[0],200

                Image:
                    color: 0,1,1,1
                    source: 'ayat_database/1_1.png'
                    pos: btn2.pos
                    size: self.parent.size
                    # size: btn2.size
                    # size: self.texture_size[0]/2, self.texture_size[1]/2


            AyaButton:
                id: btn3
                size_hint: None, None
                background_color: 0,3,3,1
                on_press: root.next_aya(btn3,2)
                size: self.parent.size[0],200

                Image:
                    color: 0,1,1,1
                    source: 'ayat_database/1_1.png'
                    pos: btn3.pos[0] ,btn3.pos[1] 
                    size: self.parent.size
                    # size: btn3.size
                    # size: self.texture_size[0]/2, self.texture_size[1]/2
                    # allow_stretch: True

    Label:
        id: head_bar
        color: 1,1,1,1
        size_hint: (1, .1)
        pos_hint: {'x':0, 'y':.90}
        #font_name: 'arial.ttf'
        canvas:
            Color:
                rgba: 0, 1, 0, 1
            Rectangle:
                pos: self.pos[0],self.pos[1]
                size: self.size[0],self.size[1]

    Label:
        id: border
        color: 0,0,0,1
        size_hint: (1, .01)
        pos_hint: {'x':0, 'y':.89}
        #font_name: 'arial.ttf'
        canvas:
            Color:
                rgba: 0, 0, 1, 1
            Rectangle:
                pos: self.pos[0],self.pos[1]
                size: self.size[0],self.size[1]


                    # center_x: self.parent.center_x
                    # center_y: self.parent.center_y
                # size_hint: (.75, .75)
                # pos_hint: {'x':.125, 'y':.02}
                # on_press: root.func()
    ''')



class Aya:
    soura = 110
    aya = 10
    ayat_max = {
       1: 7,
       2: 286,
       3: 200,
       4: 176,
       5: 120,
       6: 165,
       7: 206,
       8: 75,
       9: 129,
       10: 109,
       11: 123,
       12: 111,
       13: 43,
       14: 52,
       15: 99,
       16: 128,
       17: 111,
       18: 110,
       19: 98,
       20: 135,
       21: 112,
       22: 78,
       23: 118,
       24: 64,
       25: 77,
       26: 227,
       27: 93,
       28: 88,
       29: 69,
       30: 60,
       31: 34,
       32: 30,
       33: 73,
       34: 54,
       35: 45,
       36: 83,
       37: 182,
       38: 88,
       39: 75,
       40: 85,
       41: 54,
       42: 53,
       43: 89,
       44: 59,
       45: 37,
       46: 35,
       47: 38,
       48: 29,
       49: 18,
       50: 45,
       51: 60,
       52: 49,
       53: 62,
       54: 55,
       55: 78,
       56: 96,
       57: 29,
       58: 22,
       59: 24,
       60: 13,
       61: 14,
       62: 11,
       63: 11,
       64: 18,
       65: 12,
       66: 12,
       67: 30,
       68: 52,
       69: 52,
       70: 44,
       71: 28,
       72: 28,
       73: 20,
       74: 56,
       75: 40,
       76: 31,
       77: 50,
       78: 40,
       79: 46,
       80: 42,
       81: 29,
       82: 19,
       83: 36,
       84: 25,
       85: 22,
       86: 17,
       87: 19,
       88: 26,
       89: 30,
       90: 20,
       91: 15,
       92: 21,
       93: 11,
       94: 8,
       95: 8,
       96: 19,
       97: 5,
       98: 8,
       99: 8,
       100: 11,
       101: 11,
       102: 8,
       103: 3,
       104: 9,
       105: 5,
       106: 4,
       107: 7,
       108: 3,
       109: 6,
       110: 3,
       111: 5,
       112: 4,
       113: 5,
       114: 6
       }
    hizb = 1
    id = 100

    def next(self):
        aya = self.aya
        soura = self.soura

        if aya >= self.ayat_max[soura]-1:
            soura+=1
            if soura == 114:
                soura = 1
            aya = 0
        else:
            aya+=1

        self.aya = aya
        self.soura = soura

    def gen_name(self,ayaa):
        if ayaa.aya == 0:
            return "ayat_titles/" + str(ayaa.soura) + ".png"
        else:
            return 'ayat_database/' + str(ayaa.soura) + '_' + str(ayaa.aya) + '.png'
    
    def gen_rand_name(self,ayaa):
        return 'ayat_database/' + str(ayaa.soura) + '_' + str(randint(1,ayaa.ayat_max[ayaa.soura])) + '.png'
    
    def gen_next_name(self,ayaa):
        return 'ayat_database/' + str(ayaa.soura) + '_' + str((ayaa.aya)+1) + '.png'



class AyaLabel(Label):

    def __init__(self, **kwargs):
        super(AyaLabel, self).__init__(**kwargs)

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1, 1, 0, 1)
            Rectangle(pos=self.pos, size=self.size)

    def update(self):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1, 1, 0, 1)
            Rectangle(pos=self.pos, size=self.size)
        # self.size = w, self.children[0].texture_size[1]/2
      #self.children[0].color = yellow

class AyaButton(Button):
    
    def __init__(self, **kwargs):
        super(AyaButton, self).__init__(**kwargs)
        # self.canvas.before.clear()
        # with self.canvas.before:
        #     Color(0, 0, 1, 1)
        #     Rectangle(pos=(self.pos[0],self.pos[1]), size=(self.size[0],self.size[1]))
        
    def update(self):
        pass
      #self.children[0].color = blue
        # self.size = w, self.children[0].texture_size[1]/2
        #self.size = w+20,h
        # self.canvas.before.children[0] = Color(1,0,1,1)
        # self.canvas.before.children[1] = Color(1,0,1,1)
  
    def reset(self,dt):
        self.background_color = blue

#global contantes
Green = Color(0,1,0,1)
Blue = Color(0,0,1,1)
Yellow = Color(1,1,0,1)

green = 0,3,0,1
blue = 0,3,3,1
red = 3,0,0,1
yellow = 3,3,0,1

#glogal states
rand_num = 0
must_shuffle = True
must_refresh = False
is_title = False
x,y = 0,0

class Rotaba(FloatLayout):
    
    isfirsttime = 1
    ayaa = Aya()
    
    #ti = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Rotaba, self).__init__(**kwargs)
        
    def update(self, dt):
        lbl = self.ids.lbl
        btn = self.ids.btn
        btn2 = self.ids.btn2
        btn3 = self.ids.btn3
        btn_a = [btn,btn2,btn3]

        if must_refresh:
            lbl.children[0].source = self.ayaa.gen_name(self.ayaa)
            x2 = lbl.children[0].texture_size[0]
            y2 = lbl.children[0].texture_size[1]
            lbl.size = x2*x/x2,y2*x/x2-5
            for i in range(0,3):
                w,h = btn_a[i].children[0].size
                x2 = btn_a[i].children[0].texture_size[0]
                y2 = btn_a[i].children[0].texture_size[1]
                btn_a[i].size = x2*x/x2,(y2*x/x2)-5
            global must_refresh
            must_refresh = False

        if must_shuffle:

            for i in range(0,3):
                if i == rand_num:                                                 
                    btn_a[i].children[0].source = self.ayaa.gen_next_name(self.ayaa)
                else:
                    btn_a[i].children[0].source = self.ayaa.gen_rand_name(self.ayaa)
                    while btn_a[i].children[0].source == lbl.children[0].source\
                    or btn_a[i].children[0].source == self.ayaa.gen_next_name(self.ayaa)\
                    or btn_a[i].children[0].source == btn_a[(i+3-1)%3].children[0].source\
                    or btn_a[i].children[0].source == btn_a[(i+3+1)%3].children[0].source\
                    :
                        btn_a[i].children[0].source = self.ayaa.gen_rand_name(self.ayaa)

            global must_refresh
            must_refresh = True
            global must_shuffle 
            must_shuffle = False



        # #lbl.pos_hint = {'center_x': .1, 'center_y': .5}
        lbl.size = lbl.children[0].size
        btn.size = btn.children[0].size
        btn2.size = btn2.children[0].size
        btn3.size = btn3.children[0].size



        self.ids.lbl.update()
        self.ids.btn.update()
        self.ids.btn2.update()
        self.ids.btn3.update()

        #your initial update here
        if self.isfirsttime:
            self.isfirsttime = 0


    #functions for buttons
    def next_soura(self, *args):
        self.remove_widget(self.children[1])
        #self.remove_widget(self.children[0])
        self.add_widget(self.ids.sv)
        self.ayaa.next()
        global must_shuffle 
        must_shuffle = True
        global rand_num
        rand_num = randint(0,2)




    def next_aya(self, btn, order):
        if order == rand_num:
            self.ayaa.next()
            if self.ayaa.aya == 0:
                global is_title
                is_title = True
                self.remove_widget(self.ids.sv)

                string = self.ayaa.gen_name(self.ayaa)
                print string

                aylab = AyaLabel(id='lb',size_hint= (1 , 1))
                aylab.bind(on_touch_down= self.next_soura )
                rect = Image(id='img',source=string, pos=self.pos, size=self.size, color= (0,0,0,1) )
                self.add_widget(aylab)
                self.add_widget(rect)

            #btn.canvas.before.children[0] = Color(0, 0, 1, 1)
            #color texture
            btn.children[0].color = (0,0,1,1)
            btn.background_color = green
            Clock.schedule_once(btn.reset, .8)
            #change to green
            # btn.canvas.before.children[0] = Color(0,1,0,1)
            # btn.canvas.children[0] = Color(0,1,0,1)

            #refresh texture
            # btn.children[0].source = 
            global must_shuffle 
            must_shuffle = True
            global rand_num
            rand_num = randint(0,2)
        else:
            btn.background_color = red
            Clock.schedule_once(btn.reset, .3)


class RotabaApp(App):

    global Window
    global wdg
    def __init__(self,**kwargs):
        super (RotabaApp,self).__init__(**kwargs)
        self.wdg = None
        global x,y
        x,y = Window.size
        self.x, self.y = Window.size

    # def recreate(self):
    #     self.root.clear_widgets()
    #     self.root.add_widget(Rotaba(size= Window.size))

    def build(self):

        # def on_window_rotate(obj, degrees):
        #     pass
            
        # Window.bind(on_rotate=on_window_rotate)

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

        # Clock.schedule_interval(self.potential_on_rotate,1.0/60.0)
        Clock.schedule_interval(main_wdg.update, 1.0 / 40.0)
        return main_wdg
        
    # def potential_on_rotate(self,dt):
    #     global x,y
    #     x,y = Window.size
    #     self.wdg.ids.head_bar.text = str(x) + ',' + str(y)
    #     if self.x == y and self.y == x:
    #         self.x = x
    #         self.y = y
    #         self.recreate()


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





# from kivy.app import App
# from kivy.factory import Factory
# from kivy.lang import Builder
# from kivy.clock import Clock
# from kivy.core.window import Window


# Builder.load_string('''
# <Game@BoxLayout>:
#     id:bx
#     orientation: 'vertical'
#     Slider:
#         id: sl1
#         value: 90
#     Slider:
#         id: sl2
#         value: 100
#     Button:
#         id:btn
#         text: 'Align sliders!'
#         on_press: app.recreate()
# ''')

# class MyApp(App):
#     global Window
#     game = Factory.Game()

#     def __init__(self,**kwargs):
#         super (MyApp,self).__init__(**kwargs)
#         self.wdg = None
#         self.x, self.y = Window.size

#     def recreate(self):
#         Window.size = (self.y, self.x)
#         self.x, self.y = Window.size
#         self.root.clear_widgets()
#         self.root.add_widget(Factory.Game())

#     def build(self):
#         root = Factory.FloatLayout()
#         root.add_widget(self.game)
#         return root
#     def potential_on_rotate(self,dt):
#         x,y = Window.size
#         self.game.ids.btn.text = str(x) + ',' + str(y)
#         if self.x == y and self.y == x:
#             self.x = x
#             self.y = y
#             self.recreate()
        
# MyApp().run()   





# from kivy.app import App
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.label import Label
# from kivy.graphics import Rectangle, Color


# class MainScreen(FloatLayout, Label):

#     """MAIN WINDOW CLASS"""

#     def __init__(self, **kwargs):
#         super(MainScreen, self).__init__(**kwargs)

#         with self.canvas.before:
#             Color(0.988, 0.725, 0.074, 1, mode='rgba')
#             self.rect = Rectangle(pos=self.pos, size=self.size)
#         self.bind(size=self.update_rect)

#         self.titlos = Label(text="",
#                             bold=True,
#                             text_size=(None,None),
#                             font_size="20sp",
#                             pos_hint={'center_x': 0.5, 'center_y': .85},
#                             size_hint_y=None,
#                             size = self.size,
#                             height=self.texture_size[1],
#                             halign="center",
#                             valign = "middle",
#                             color=(0.055, 0.235, 0.541, 1))

#         self.add_widget(self.titlos)
#         self.bind(size=self.update_orientation)

#     def update_rect(self, *args):
#         """FUNCTION TO UPDATE THE RECATANGLE OF CANVAS TO FIT THE WHOLE SCREEN OF MAINSCREEN ALWAYS"""
#         self.rect.pos = self.pos
#         self.rect.size = self.size

#     def update_orientation(self, *args):
#         """FUNCTION TO UPDATE THE SCREEN CONTENTS WHEN THE WINDOW SIZE CHANGES"""
#         if self.parent.size[1] > self.parent.size[0]:
#             self.titlos.text = "This is\nPortrait\nOrientation"
#         else:
#             self.titlos.text = "This is Landscape Orientation"

#         # This is just for checking. Not essential to the program.
#         print("Width:", self.parent.size[0], ", Height:", self.parent.size[1])



# class main(App):
#     """BUILDING THE APP"""
#     def build(self):
#         return MainScreen()

# if __name__ == "__main__":
#     main().run()
