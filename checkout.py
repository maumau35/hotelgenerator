from folderfinder import findfolder
import json
import os
import roomtemplates
import os
def checkout(personname):

    hotelfolder = findfolder()

    with open(hotelfolder+'\\'+'custdata.json','r') as f:
        customersdata = json.loads(f.read())
        f.close()
    if customersdata[personname] == "":
        return
    custdata = customersdata[personname]


    roomnumber = custdata['stayingin']


    with open(hotelfolder + "\\" + 'roomfile.json', "r") as f:
        room = 'room ' + str(roomnumber)
        rooms = json.loads(f.read())
        roomdata = rooms[room]
        f.close()
    typeroom = roomdata['roomtype']
    with open(hotelfolder+'\\'+'roomfile.json', 'w') as f:
        if typeroom == 'normal':
            rooms[room] = roomtemplates.jsonroomtemp1
            roomtype = 1
        elif typeroom == 'suite':
            rooms[room] = roomtemplates.jsonroomtemp2
            roomtype = 2
        else:
            rooms[room] = roomtemplates.jsonroomtemp3
            roomtype = 3
        json.dump(rooms, f, indent=4)
        f.close()
    with open(hotelfolder+'\\'+'hoteldata.json','r') as f:
        hoteldata = json.loads(f.read())
        f.close()
    with open(hotelfolder+'\\'+'hoteldata.json','w') as f:
        if roomtype == 1:
            hoteldata['normalroomsavb'] = hoteldata['normalroomsavb'] + 1
        elif roomtype == 2:
            hoteldata['suitesavb'] = hoteldata['suitesavb'] + 1
        else:
            hoteldata['luxurysuitesavb'] = hoteldata['luxurysuitesavb'] + 1
        json.dump(hoteldata, f)
        f.close()
    del customersdata[personname]
    with open(hotelfolder+'\\'+'custdata.json','w') as f:
        json.dump(customersdata, f, indent=4)
        f.close()

