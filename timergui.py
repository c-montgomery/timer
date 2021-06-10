import tkinter as tk
from tkinter.ttk import Combobox
from timer import Egg_timer
from pygame import mixer

class Window():
    def __init__(self, arg):
        self.arg = tk.Tk()
        self.arg.title('Egg timer')
        # self.button1 needs to change command to start_timer(5) after testing
        self.button1 = tk.Button( self.arg, text = '5 minutos', command=lambda: self.start_timer('timer1', 1))
        self.button1.pack()
        self.arg.bind('<Key>', self.key_press)
        self.arg.mainloop()

    def start_timer(self, name, minutes):
        name = Egg_timer()
        name.start_timer(minutes)
        
    def key_press(self, event):
        key = event.char
        if key:
            mixer.music.stop()

         
win1 = Window('Ass')
