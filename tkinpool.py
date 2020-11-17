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
root.geometry(str(screensizex)+"x"+str(screensizey)), root.title('Pool')


lab = Label(root)
lab.config(text='welcome',font = ('Helvetica',40))

def normalconfig():
    lab.config(background='yellow',
               font = ('Helvetica',10))

def pool1():

    with open(hotelfolder + '\\' + 'pool.json', 'r') as f:
        pool = json.loads(f.read())
        pool.pop('start', None)
        pool = json.dumps(pool, indent=4)
        f.close()

    lab.config(text=pool,
               background='Blue',
               font=('Helvetica', 15),
               anchor='center')
    lab.pack(side=LEFT, expand=YES, fill=BOTH)


    root.after(3000, pool1)  # run itroot again after 1000 ms

menu = Menu()

exit = Menu(menu)
exit.add_command(label='Exit', command=root.quit)
menu.add_cascade(label= 'Exit', menu= exit)
# run first time
pool1()

root.mainloop()