from tkinter import *
import datetime
from folderfinder import findfolder
hotelfolder = findfolder()
import ctypes
import json
user32 = ctypes.windll.user32
screensizex = int(0.2*user32.GetSystemMetrics(0))
screensizey= int(0.95*user32.GetSystemMetrics(1))
root = Tk()
root.geometry(str(screensizex)+"x"+str(screensizey)), root.title('City')


lab = Label(root)
lab.config(text='welcome',font = ('Helvetica',40))

def normalconfig():
    lab.config(background='yellow',
               font = ('Helvetica',10))

def city1():

    with open(hotelfolder + '\\' + 'city.json', 'r') as f:
        city = json.loads(f.read())
        city.pop('start', None)
        city = json.dumps(city, indent=4)
        f.close()

    lab.config(text=city,
               background='Green',
               font=('Helvetica', 12),
               anchor='center')
    lab.pack(side=LEFT, expand=YES, fill=BOTH)
    root.after(3000, city1)  # run itroot again after 1000 ms



menu = Menu()

exit = Menu(menu)
exit.add_command(label='Exit', command=root.quit)
menu.add_cascade(label= 'Exit', menu= exit)
# run first tim
city1()
root.mainloop()