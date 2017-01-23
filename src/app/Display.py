'''
Created on 22 Jan 2017

@author: chrisdoherty
'''

from kivy.config import Config
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

Config.set('graphics', 'fullscreen', 'auto')

class DisplayLayout(FloatLayout):
    
    def __init__(self, **kwargs):
        super(DisplayLayout, self).__init__(**kwargs)
        
        self.bind(size=self._update_button, pos=self._update_button)
        
        self.green = (0, 1, 0, 1)
        self.red = (1, 0, 0, 1)
        
        self.button = Button(size=self.size, pos=self.pos, background_color=self.green)
        self.button.bind(on_press=self.button_pressed)
        self.add_widget(self.button)
        
    def _update_button(self, instance, value):
        self.button.pos = instance.pos
        self.button.size = instance.size
    
    ''' Kills the app when the button is pressed. '''
    def button_pressed(self, obj):
        App.get_running_app().stop()
        
    ''' Changes us to occupied state '''
    def occupied(self):
        self.button.background_color = self.red
    
    ''' Changes us to unoccupied state '''
    def unoccupied(self):
        self.button.background_color = self.green

class Display(App):
    def build(self):
        self.root = root = DisplayLayout()
        return root
    
    def notify(self, hub_room):
        if str(hub_room.state_) == 'UnoccupiedState':
            self.root.unoccupied()
        else:
            self.root.occupied()

if __name__ == '__main__':
    Display().run()