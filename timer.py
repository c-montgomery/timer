import time
from selenium.webdriver import Chrome
import winsound
from audioplayer import AudioPlayer
import tkinter as tk


root = tk.Tk()
root.geometry('600x600')

user_input = tk.Label()
user_input.pack()
# Requests number of minutes
requested_units = int(input('Enter number of minutes\n'))*60
start_time = time.time()
elapsed_time = (time.time()-start_time)
x = elapsed_time



while int(x) < int(requested_units):
	elapsed_time = (time.time()-start_time)
	x = elapsed_time
	print(x)


# winsound.Beep(5000,1000)
sound_machine = AudioPlayer("C:/Users/craym/Desktop/alarm.wav")
sound_machine.play(block=True)

