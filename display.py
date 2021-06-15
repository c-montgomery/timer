from tkinter import *
import time



root = Tk()
label1 = Label(root)
label1.pack()

start = time.time()

def update():
    elapsed = (round(time.time(),1) - round(start, 1))*2
    label1.config(text=round(elapsed))
    root.after(1000, update)
update()

root.mainloop()