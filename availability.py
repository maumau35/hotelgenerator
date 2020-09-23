import json
import os


def availableroom(roomtype):
    if roomtype == 'normal':
        roomtypenec = 'normalroomsavb'
    elif roomtype == 'suite':
        roomtypenec = 'suitesavb'
    else:
        roomtypenec ='luxurysuitesavb'
    with open('lastchoice.txt', 'r') as f:
        hotelsize = f.read()

        f.close()
    if int(hotelsize) == 3:
        hotelsizename = 'big'
    elif int(hotelsize) == 2:
        hotelsizename = 'medium'
    else:
        hotelsizename = 'small'
    with open('hotelnumber' + hotelsizename + '.txt', 'r') as f:
        hotelnumber = int(f.read()) - 1
        f.close()
    cwd = os.getcwd()
    hotelfolder = cwd + '\\' + hotelsizename + str(hotelnumber)
    with open(hotelfolder + '\\' + 'hoteldata.json', 'r') as f:
        hoteldata = json.loads(f.read())

        f.close()
    if int(hoteldata[roomtypenec]) != 0:
        roomnumber = 1
        currentfloor = 0
        while currentfloor <= int(hoteldata['floors']):
            for _ in range(int(hoteldata['rooms'])):
                stringroom = str(roomnumber)
                if len(stringroom) == 1:
                    stringroom = '0' + stringroom
                with open(hotelfolder+"\\" + 'roomfile.json', "r") as f:
                    room = 'room '+str(currentfloor) + stringroom
                    roomsdata = json.loads(f.read())
                    roomdata = roomsdata[room]
                    f.close()
                if roomtype == roomdata['roomtype'] and roomdata['status'] == 'available':
                    avbroom = str(currentfloor)+stringroom

                    return avbroom
                else:
                    navbroom = str(currentfloor)+stringroom

                if roomnumber == hoteldata['rooms']:
                    roomnumber = 1
                    currentfloor += 1
                else:
                    roomnumber += 1
    else:

        return 'room unavb'
