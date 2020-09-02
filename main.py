from roomgen import roommaker
from chooseoption import chooseoption
from folderfinder import findfolder
from reservation import reservation
from cleaners import cleaners
from checkout import checkout
import random
from cls import cls
import time
import json
schedule={}


def start():
    hotelsize = chooseoption()
    roommaker(hotelsize)
    hotelfolder = findfolder()


    with open(hotelfolder + '\\' + 'hoteldata.json', 'r') as f:
        hoteldata = json.loads(f.read())
        f.close()
    with open(hotelfolder + '\\' + 'schedule.json', 'w') as f:
        for x in range(100):
            cleantime = 240+x*480
            schedule.update({cleantime:'clean1'})
        json.dump(schedule,f)
        f.close()
    totalrooms = (hoteldata['totalrooms'])
    totalcustomers = totalrooms * random.uniform(0.6,0.8)
    custdata = {}
    with open(hotelfolder + '\\' + 'custdata.json', 'w') as f:

        for _ in range(int(totalcustomers)):
            p, customer = reservation()
            print(customer)

            if customer['customernamewospace'] != "":
                customername = customer['customernamewospace']
                custdata[customername] = customer


        json.dump(custdata, f, indent=4)

        f.close()

    print('end')
    return totalcustomers


def counter():
    totalcustomers = start()
    persperit = totalcustomers/4800
    hotelfolder = findfolder()

    count = 1
    liveupdate = []

    while True:

        randomnumber = random.uniform(0, 1)


        if randomnumber < persperit:

            with open(hotelfolder + '\\' + 'custdata.json', 'r') as f:
                custdata = json.loads(f.read())
                f.close()
            p, customer = reservation()
            if p == 1:
                liveupdate.append('there was no room available for '+customer)
            else:
                customername1 = customer['customernamewospace']
                custdata[customername1] = customer
                customername = customer['customername']
                customerroom = customer['stayingin']
                enterupdate = '{0} entered the hotel at {1} and checked in into room {2}'.format(customername, count,
                                                                                                 customerroom)
                liveupdate.append(enterupdate)
                with open(hotelfolder + '\\' + 'custdata.json', 'w') as f:
                    json.dump(custdata, f, indent=4)
                    f.close()


        with open(findfolder()+'\\'+'schedule.json', 'r') as f:
            schedule = json.loads(f.read())

            if str(count) in schedule:

                if 'clean1' in schedule[str(count)]:
                    cleaners()
                    cleanupdate = 'the rooms were cleaned at {0}'.format(count)
                    liveupdate.append(cleanupdate)

                elif schedule[str(count)].endswith(' checkout'):
                    personname = schedule[str(count)]
                    personname = personname[:-9]
                    checkout(personname)
                    checkoutupdate = '{0} checked out at {1}'.format(personname, count)
                    liveupdate.append(checkoutupdate)

        f.close()
        if len(liveupdate) >= 4:
            lenliveupdate = len(liveupdate) - 3
            for _ in range(lenliveupdate):
                liveupdate.pop(0)
        time.sleep(0.0001)

        if (count/40).is_integer() or count == 1:
            cls()
            with open(hotelfolder + '\\' + 'hoteldata.json', 'r') as f:
                hoteldata = json.loads(f.read())
                f.close()
                totalrooms, totalroomsavb, totalnormal, normalavb, totalsuite, suiteavb, totallux, luxavb = hoteldata['totalrooms'], hoteldata['normalroomsavb'] + hoteldata['suitesavb'] + hoteldata['luxurysuitesavb'],hoteldata['normalrooms'],hoteldata['normalroomsavb'],hoteldata['suites'],hoteldata['suitesavb'],hoteldata['luxurysuites'],hoteldata['luxurysuitesavb']
                livedata = ('''
                total rooms: {0}   total rooms available: {1}
                normal rooms: {2}  normal rooms available: {3}
                suites: {4}        suites available: {5}
                luxury suites {6}  luxury suites available: {7}'''.format(totalrooms, totalroomsavb, totalnormal,
                                                                          normalavb, totalsuite, suiteavb, totallux,
                                                                          luxavb))

            print(livedata)
            for x in range(len(liveupdate)):

                print(liveupdate[x])


        count += 1


        with open(findfolder()+'\\'+'hoteldata.json', 'r') as f:
            hoteldata = json.loads(f.read())
            f.close()

        with open(findfolder()+'\\'+'time.txt', 'w') as f:
            f.write(str(count))
            f.close()
counter()

