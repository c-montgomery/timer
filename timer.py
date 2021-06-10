import time
from pygame import mixer
import keyboard
import pygame
import time

class Egg_timer:
    '''It's an egg timer'''
    def __init__(self):
        self.minutes = 1
        self.elapsed_seconds = 0

    '''Starts counting time, calls play_alarm function'''
    def start_timer(self, minutes):
        seconds_set = int(minutes)*60
        start_timer = time.time()
        #Does line 18 need to be there?
        elapsed_seconds = round(time.time() - start_timer, 2)
        while int(elapsed_seconds) < int(seconds_set):
            elapsed_seconds = round(time.time() - start_timer, 2)
            time.sleep(.01)
            print(round(elapsed_seconds, 2))
        self.play_alarm()
    '''initializes audio player, plays audio until space is pressed'''
    def play_alarm(self):
        mixer.init()
        alarm_audio = mixer.music.load("C:/Users/craym/Desktop/alarm2.wav")
        mixer.music.play(loops=-1)
        
        #while keyboard.is_pressed('space')==True:
        #   mixer.music.stop()

    

