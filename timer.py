import time
from pygame import mixer
import keyboard
import pygame

class Egg_timer:
    '''It's an egg timer'''
    def __init__(self):
        self.minutes = 1
        self.elapsed_seconds = 0

    def start_timer(self):
        seconds_set = int(self.minutes)*60
        start_timer = time.time()
        while int(self.elapsed_seconds) < int(seconds_set):
            self.elapsed_seconds = round(time.time() - start_timer, 2)
            print(round(self.elapsed_seconds, 2))
        self.play_alarm()

    def play_alarm(self):
        mixer.init()
        alarm_audio = mixer.music.load("C:/Users/craym/Desktop/alarm2.wav")
        while keyboard.is_pressed('space')==False:
            mixer.music.play(loops=-1)
        mixer.music.stop()

    def set_timer(self):
       self.minutes = input('How many minutes? \n')
       self.start_timer()

