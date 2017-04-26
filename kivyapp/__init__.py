
from kivy.app import App

from kivy.uix.pagelayout import PageLayout

class GridlayoutApp(App):
    def build(self):
        return PageLayout()

flApp = GridlayoutApp()
flApp.run()