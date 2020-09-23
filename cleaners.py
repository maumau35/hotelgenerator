import json
import time
from folderfinder import findfolder

def cleaners():


    hotelfolder = findfolder()
    with open(hotelfolder+ '\\'+'time.txt', 'r') as f:
        time1 = f.read()
        f.close()
    with open(hotelfolder + '\\' + 'hoteldata.json', 'r') as f:
        hoteldata = json.loads(f.read())
        print(hoteldata)

        f.close()
    roomnumber = 1
    currentfloor = 0
    with open(hotelfolder + "\\" + 'roomfile.json', "r") as f:
        roomsdata = json.loads(f.read())
        f.close()


    while currentfloor <= int(hoteldata['floors']):
        for _ in range(int(hoteldata['rooms'])):
            stringroom = str(roomnumber)
            if len(stringroom) == 1:
                stringroom = '0' + stringroom

                room = 'room ' + str(currentfloor) + stringroom


                roomdata = roomsdata[room]

            if roomdata['occupantsstatus'] == 'away':
                roomdata['lastclean'] = time1

                roomsdata[room] = roomdata



            else:
                navbroom = str(currentfloor) + stringroom

            if roomnumber == hoteldata['rooms']:
                roomnumber = 1
                currentfloor += 1
            else:
                roomnumber += 1


    with open(hotelfolder + "\\" + 'roomfile.json', "w") as f:
        json.dump(roomsdata, f, indent=4)
        f.close()







