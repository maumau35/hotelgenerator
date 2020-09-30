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
    with open(hotelfolder + "\\" + 'roomfile.json', "r") as f:
        roomsdata = json.loads(f.read())
        f.close()
    with open(findfolder() + '\\' + 'custdata.json', 'r') as f:
         customersdata = json.loads(f.read())
         f.close()
    customerlist = [*customersdata]
    maxlen = len(customerlist)
    for x in range(maxlen):
        customername = customerlist[x]
        customer = customersdata[customername]
        room = 'room '+ customer['stayingin']
        roomdata = roomsdata[room]
        if customer['status'] != 'inroom':
            roomdata['lastclean'] = time1
            roomsdata[room] = roomdata


    with open(hotelfolder + "\\" + 'roomfile.json', "w") as f:
        json.dump(roomsdata, f, indent=4)
        f.close()







