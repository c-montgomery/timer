import time
from audioplayer import AudioPlayer
import keyboard

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
        sound_machine = AudioPlayer("C:/Users/craym/Desktop/alarm.wav")
        while keyboard.is_pressed('space')==False:
            sound_machine.play(loop=True, block=True)
        sound_machine.stop()    

    def set_timer(self):
       self.minutes = input('How many minutes? \n')
       self.start_timer()

