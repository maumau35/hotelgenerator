from tkinter import *
import datetime
from folderfinder import findfolder
hotelfolder = findfolder()
import pprint
import ctypes
import json
user32 = ctypes.windll.user32
screensizex = int(0.2*user32.GetSystemMetrics(0))
screensizey= int(0.95*user32.GetSystemMetrics(1))
root = Tk()
root.geometry(str(screensizex)+"x"+str(screensizey)), root.title('Restaurant')

with open(hotelfolder + '\\' + 'restaurant.json', 'r') as f:
    restaurant = json.loads(f.read())
    f.close()
lab = Label(root)
lab.config(text='welcome',font = ('Helvetica',40))

def normalconfig():
    lab.config(background='yellow',
               font = ('Helvetica',10))

def restaurant1():

    with open(hotelfolder + '\\' + 'restaurant.json', 'r') as f:
        restaurant = json.loads(f.read())
        restaurant.pop('start', None)
        restaurant = json.dumps(restaurant, indent=4)
        f.close()


    lab.config(text=restaurant,
               background='Yellow',
               font=('Helvetica', 15),
               anchor='w')
    lab.pack(side=LEFT, expand=YES, fill=BOTH)

    # lab['text'] = time
    root.after(3000, restaurant1)  # run itroot again after 1000 ms


menu = Menu()

exit = Menu(menu)
exit.add_command(label='Exit', command=root.quit)
menu.add_cascade(label= 'Exit', menu= exit)
# run first time
restaurant1()

root.mainloop()