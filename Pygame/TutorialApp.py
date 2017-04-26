

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class ScatterTextWidget(BoxLayout):
    pass
    
class TutorialApp(App):
    def build(self):
        b = BoxLayout(orientation = 'vertical')
        t = TextInput(font_size = 50 , 
                                size_hint_y=None,
                                height=200,
                                text ='default')
        
        f = FloatLayout()
        s = Scatter()
        l = Label(text="default",
                        font_size = 100)

        t.bind(text=l.setter('text'))

        f.add_widget(s)
        s.add_widget(l)

        b.add_widget(t)
        b.add_widget(f)
        return b 

def some_function(*args):
    print 'text changed'

if __name__ == "__main__":
     TutorialApp().run()