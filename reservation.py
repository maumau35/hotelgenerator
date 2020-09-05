import availability
import generatecustomer
import random
import json
from folderfinder import findfolder
import os
def reservation():

    hotelfolder = findfolder()
    with open(findfolder() + '\\' + 'schedule.json', 'r') as f:
        schedule = json.loads(f.read())
        f.close()

    customernamewospace, customername, desiredroom = generatecustomer.gencustomer()

    jsoncustomer = {
        'customernamewospace': customernamewospace,
        'customername': customername,
        'desiredroom': desiredroom,
        'stayingin': '',
        'inroom': '',
        'checksout': '',
        'goesout': ''
    }

    custwantroom = desiredroom
    avbwantedroom = availability.availableroom(custwantroom)


    if avbwantedroom == 'room unavb':

        return 1, customername
    else:
        with open(hotelfolder + "\\" + 'roomfile.json', "r") as f:
            room = 'room ' + avbwantedroom
            roomsdata = json.loads(f.read())
            roomdata = roomsdata[room]
            f.close()
        roomdata['status'] = 'not'
        roomdata['occupants'] = customername
        roomdata['occupantsstatus'] = 'home'
        roomsdata[room] = roomdata
        with open(hotelfolder + "\\" + 'roomfile.json', "w") as f:
            json.dump(roomsdata, f, indent=4)
            f.close()

        with open(hotelfolder+'\\'+'hoteldata'+'.json', 'r') as f:
            hoteldata = json.loads(f.read())
            f.close()
        if custwantroom == 'normal':
            hoteldata['normalroomsavb'] = int(hoteldata['normalroomsavb']) - 1
        elif custwantroom == 'suite':
            hoteldata['suitesavb'] = int(hoteldata['suitesavb']) - 1
        elif custwantroom == 'luxury suite':
            hoteldata['luxurysuitesavb'] = int(hoteldata['luxurysuitesavb']) - 1
        else:



            pass

        with open(hotelfolder+'\\'+'hoteldata'+'.json', 'w') as f:
            json.dump(hoteldata, f)
            f.close()


        with open(findfolder() + '\\' + 'time.txt', 'r') as f:
            time = float(f.read())
            f.close()
        checkouttime = int(random.uniform(10, 4800) + time)
        for _ in range(10000):
            if checkouttime not in schedule:
                break
            else:
                checkouttime = int(random.uniform(500, 5000) + time)

        schedule.update({checkouttime: customernamewospace + ' checkout'})
        with open(findfolder() + '\\' + 'schedule.json', 'w') as f:
            json.dump(schedule, f, indent=4)
            f.close()
        jsoncustomer['stayingin'] = avbwantedroom

        jsoncustomer['inroom'] = 'yes'
        jsoncustomer['checksout'] = checkouttime

        return 2, jsoncustomer


