'''
Created on 22 Jan 2017

@author: chrisdoherty
'''

import tkinter as tk

class Display(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.unoccupied()
        
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        
        self.geometry('%dx%d+%d+%d' % (ws, hs, 3, 3))
        
    def occupied(self):
        self.winfo_toplevel().configure(bg = '#F00')
    
    def unoccupied(self):
        self.winfo_toplevel().configure(bg = '#0F0')
    
    def notify(self, hub_room):
        if str(hub_room.state_) == 'UnoccupiedState':
            self.unoccupied()
        else:
            self.occupied()

if __name__ == '__main__':
    Display().mainloop()
    
    