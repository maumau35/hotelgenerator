import time
import json
import os
import random
import roomtemplates
import chooseoption
from folderfinder import findfolder


def roommaker(hotelsize):
    global jsonroomtemp

    if hotelsize.isnumeric:
        hotelsize=int(hotelsize)

        if hotelsize == 1:
            floorsmin = 2

            multiplier = 1
            roomonfloor = 5
            name = 'small'

        if hotelsize == 2:
            floorsmin = 3

            multiplier = 1.5
            roomonfloor = 10
            name = 'medium'


        if hotelsize == 3:

            floorsmin = 4
            multiplier = 2
            roomonfloor = 20

            name = 'big'

        else:
            print('fail')
        cwd = os.getcwd()
        print(cwd)
        hotelnumberfile = open("hotelnumber" + name + ".txt", "r").read()
        hotelnumber = int(hotelnumberfile)
        hoteldir = name + str(hotelnumber)
        hotelnumberfile = open("hotelnumber" + name + ".txt", "w")
        hotelnumberfile.write(str(hotelnumber + 1))
        hotelnumberfile.close()
        os.makedirs(hoteldir)
        randomnumber = int(random.uniform(0, 3)*multiplier)
        floors = floorsmin + randomnumber
        currentfloor = 0
        print(floors)
        roomnumber = 1
        suites = 0
        normalrooms = 0
        luxurysuites = 0
        rooms = {}
        with open(findfolder()+ "//" + 'roomfile.json', 'w') as f:
            while currentfloor <= floors:
                for _ in range(roomonfloor):
                    stringroom = str(roomnumber)
                    if len(stringroom) == 1:
                        stringroom = '0' + stringroom
                    room = 'room ' + str(currentfloor) + stringroom


                    randomroomtype = random.uniform(0, 3)
                    if randomroomtype < 2:
                        rooms[room] = roomtemplates.jsonroomtemp1
                        normalrooms += 1
                    elif randomroomtype < 2.6:
                        rooms[room] = roomtemplates.jsonroomtemp2
                        suites += 1
                    else:
                        rooms[room] = roomtemplates.jsonroomtemp3
                        luxurysuites += 1


                    if roomnumber == roomonfloor:
                        roomnumber = 1
                        currentfloor += 1
                    else:
                        roomnumber += 1
            json.dump(rooms, f, indent=4)
            f.close()

        with open(cwd + "\\" + hoteldir + "\\" + 'hoteldata.json', "w") as f:
            hoteldatajson = {
                'totalrooms':(floors+1)*roomonfloor,
                'floors':floors,
                'rooms':roomonfloor,
                'normalrooms':normalrooms,
                'suites':suites,
                'luxurysuites':luxurysuites,
                'normalroomsavb': normalrooms,
                'suitesavb': suites,
                'luxurysuitesavb': luxurysuites
            }
            json.dump(hoteldatajson, f)
            f.close()
        with open(cwd + "\\" + hoteldir + "\\" + 'time.txt', "w") as f:
            f.write('0')
            f.close()

    else:
        print('error, please enter a number')
        roommaker()






