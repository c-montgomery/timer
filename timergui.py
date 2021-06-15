import tkinter as tk
from tkinter.ttk import Combobox
from timer import EggTimer
from pygame import mixer
from tkinter import *



class Window():
    def __init__(self, arg):
        self.arg = tk.Tk()
        self.arg.title('Egg timer')
        '''Creates display for timer'''
        

        

        # self.button1 needs to change command to start_timer(5) after testing
        self.button1 = tk.Button( self.arg, text = '5 minutos', command=lambda: self.start_timer('timer1', 1))
        self.button1.pack()

        self.button1 = tk.Button( self.arg, text = '15 minutos', command=lambda: self.start_timer('timer1', 15))
        self.button1.pack()
        self.name = EggTimer()
        
        self.time_elapsed = 0

        self.label = tk.Label(self.arg, text = self.time_elapsed)
        self.label.pack()

        '''listen for keypress is bound to main window'''
        self.arg.bind('<Key>', self.key_press)
        self.arg.mainloop()

    '''creates EggTimer and starts counting'''
    def start_timer(self, name, minutes):
        self.name.start_timer(minutes)
        
    '''Updates countdown display'''
    # def update_timer():
        
    #     self.label.config(text = self.name.elapsed_seconds)
    #     self.arg.after(100, self.update_timer)

    '''listens for keypress and stops alarm'''    
    def key_press(self, event):
        key = event.char
        if key:
            mixer.music.stop()

    


win1 = Window('window1')
