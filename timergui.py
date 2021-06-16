import tkinter as tk
from tkinter.ttk import Combobox
from timer import EggTimer
from pygame import mixer
from tkinter import *
import time


class Window():
    def __init__(self, name):
        
        '''Creates display for timer'''
        self.name = tk.Tk()
        # self.button1 needs to change command to start_timer(5) after testing
        self.button1 = tk.Button( self.name, text = '5 minutos', command=lambda: self.start_timer('timer1', 1))
        self.button1.pack()

        self.button1 = tk.Button( self.name, text = '15 minutos', command=lambda: self.start_timer('timer1', 15))
        self.button1.pack()
        self.egg = EggTimer()
        self.start_time = time.time()
        self.current_time = time.time()
        self.time_elapsed = 0

        self.label = tk.Label(self.name, text = self.time_elapsed)
        self.label.pack()
        
        self.name.mainloop()

    '''creates EggTimer and starts counting'''
    def start_timer(self, name, minutes):
        self.current_time = time.time()
        self.update_timer(self.current_time)
        
        self.time_elapsed = round(self.current_time ,1) - round(self.start_time, 1)
        
    '''Updates countdown display'''
    def update_timer(self, time):
        
        self.label.config(text = time)
        self.name.after(1000, self.update_timer())

    '''listens for keypress and stops alarm'''    
    def key_press(self, event):
        key = event.char
        if key:
            mixer.music.stop()
# self.bind('<Key>', self.key_press)

win = Window('Bilbo')