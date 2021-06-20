import tkinter as tk
from timer import EggTimer
from pygame import mixer
import time


class Window():
    def __init__(self, name):
        '''Creates display for timer'''
        self.name = tk.Tk()
        self.name.iconbitmap('favicon.ico')
        self.name.title('Timer')
        self.egg = EggTimer()
        self.start_time = 0
        self.current_time = 0
        self.time_elapsed = 0
        self.is_running = False
        self.minutes_set = 0
        self.is_playing = False

        self.label = tk.Label(self.name, text=self.time_elapsed)
        self.label.pack()
      
        self.button1 = tk.Button(
            self.name, text='5 minutos', command=lambda: self.start_timer('timer1', 5))
        self.button1.pack()

        self.button1 = tk.Button(
            self.name, text='15 minutos', command=lambda: self.start_timer('timer1', 15))
        self.button1.pack()

        self.name.bind('<Key>', self.key_press)
        self.name.mainloop()

    '''creates EggTimer and starts counting'''

    def start_timer(self, name, minutes):
        self.start_time = time.time()
        self.current_time = time.time()
        self.minutes_set = minutes
        self.update_timer()

    '''Updates countdown display'''
    '''needs way to reset variables after timer stopped'''

    def after_stop(self):
        while self.is_playing:
            print('BROKE')
            break
        else:
            self.update_timer()

    def update_timer(self):
        self.label.config(text=round(self.time_elapsed, 1))

        self.name.after(100, self.after_stop)
        self.time_elapsed = time.time() - self.start_time
        if self.time_elapsed >= self.minutes_set * 60:
            self.egg.play_alarm()
            self.is_playing = True

    '''listens for keypress and stops alarm'''

    def key_press(self, event):
        key = event.char
        if key:
            mixer.music.stop()


win = Window('Bilbo')
