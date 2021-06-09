import tkinter as tk
from tkinter.ttk import Combobox
from timer import Egg_timer

class Window:
    '''Creates instance of egg timer gui'''
    def __init__(self, name):
        self.time = 1
        self.name = name

    def create_timer(name, minutes ):
        name = Egg_timer()
        name.start_timer(minutes)

    '''Variables for audio choice combobox'''
    audio_tracks = ['soft', 'loud']

    '''create window, set size and title'''
    root = tk.Tk()
    root.geometry('300x300')
    root.title('Egg Timer')

    '''create labels, buttons and combobox'''
    instruction_label = tk.Label(root, text = 'Input an integer or choose a preset')
    instruction_label.pack()

    '''creates 'quick' buttons and packs them'''
    quick5 = tk.Button(root, text = '5 minutes', command=create_timer('timer1', 5))
    quick15 = tk.Button(root, text = '15 minutes', command=create_timer('timer2', 15))

    quick5.pack()
    quick15.pack()

    

    root.mainloop()

win1 = Window('freddy')