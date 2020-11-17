from tkinter import *
import datetime
from folderfinder import findfolder
hotelfolder = findfolder()
import ctypes
import json
user32 = ctypes.windll.user32
screensizex = int(0.2*user32.GetSystemMetrics(0))
screensizey= int(0.4*user32.GetSystemMetrics(1))
root = Tk()
root.geometry(str(screensizex)+"x"+str(screensizey)), root.title('Hotel')


lab = Label(root)
lab.config(text='welcome',font = ('Helvetica',40))

def normalconfig():
    lab.config(background='yellow',
               font = ('Helvetica',10))
def hotelstats():

    with open(hotelfolder + '\\' + 'hoteldata.json', 'r') as f:
        hoteldata = json.loads(f.read())
        f.close()
        totalrooms, totalroomsavb, totalnormal, normalavb, totalsuite, suiteavb, totallux, luxavb, revenue, weekrevenue = \
        hoteldata['totalrooms'], hoteldata['normalroomsavb'] + hoteldata['suitesavb'] + hoteldata['luxurysuitesavb'], \
        hoteldata['normalrooms'], hoteldata['normalroomsavb'], hoteldata['suites'], hoteldata['suitesavb'], hoteldata[
            'luxurysuites'], hoteldata['luxurysuitesavb'], hoteldata['revenue'], hoteldata['lastweekrev']
        livedata = ('''
                   total rooms: {0}
                   total rooms available: {1}
                   normal rooms: {2}  
                   normal rooms available: {3}
                   suites: {4}        
                   suites available: {5}
                   luxury suites: {6} 
                   luxury suites available: {7}
                   last week's revenue: {8}
                   total revenue: {9}  '''.format(totalrooms, totalroomsavb, totalnormal,
                                                                          normalavb, totalsuite, suiteavb, totallux,
                                                                          luxavb, revenue, weekrevenue))
        lab.config(text=livedata,
                   background='Blue',
                   font=('Helvetica', 20),
                   anchor='e')
        lab.pack(side=RIGHT, expand=YES, fill=BOTH)

        # lab['text'] = time



        root.after(3000, hotelstats)


menu = Menu()

exit = Menu(menu)
exit.add_command(label='Exit', command=root.quit)
menu.add_cascade(label= 'Exit', menu= exit)
# run first time
hotelstats()

root.mainloop()