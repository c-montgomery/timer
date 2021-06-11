import tkinter as tk
from tkinter.ttk import Combobox
from timer import EggTimer
from pygame import mixer

class Window():
    def __init__(self, arg):
        self.arg = tk.Tk()
        self.arg.title('Egg timer')

        # self.button1 needs to change command to start_timer(5) after testing
        self.button1 = tk.Button( self.arg, text = '5 minutos', command=lambda: self.start_timer('timer1', 5))
        self.button1.pack()

        '''listen for keypress is bound to main window'''
        self.arg.bind('<Key>', self.key_press)
        self.arg.mainloop()
        
    '''creates EggTimer and starts counting'''
    def start_timer(self, name, minutes):
        name = EggTimer()
        name.start_timer(minutes)
    '''Updates countdown display'''
    def update_timer():
        pass
    '''listens for keypress and stops alarm'''    
    def key_press(self, event):
        key = event.char
        if key:
            mixer.music.stop()

         
win1 = Window('window1')
