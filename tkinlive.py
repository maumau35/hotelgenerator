from tkinter import *
import datetime
from folderfinder import findfolder
hotelfolder = findfolder()
import ctypes
import json
user32 = ctypes.windll.user32
screensizex = int(0.2*user32.GetSystemMetrics(0))
screensizey= int(0.5*user32.GetSystemMetrics(1))
root = Tk()
root.geometry(str(screensizex)+"x"+str(screensizey)), root.title('Livefeed.json')


lab = Label(root)
lab.config(text='welcome',font = ('Helvetica',40))

def normalconfig():
    lab.config(background='yellow',
               font = ('Helvetica',10))

def city1():

    with open(hotelfolder + '\\' + 'livefeed.json', 'r') as f:
        city = (f.read())
        f.close()


    lab.config(text=city,
               background='Blue',
               font=('Helvetica', 13),
               anchor='n')
    lab.pack(side=LEFT, expand=YES, fill=BOTH)
    root.after(10000, city1)  # run itroot again after 1000 ms



menu = Menu()

exit = Menu(menu)
exit.add_command(label='Exit', command=root.quit)
menu.add_cascade(label= 'Exit', menu= exit)
# run first tim
city1()
root.mainloop()