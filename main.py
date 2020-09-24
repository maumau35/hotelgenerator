from roomgen import roommaker
from chooseoption import chooseoption
from folderfinder import findfolder
from reservation import reservation
from cleaners import cleaners
from checkout import checkout
from custactions import custactions
import random
from money import money
from breakfast import breakfast
from hoteltime import hoteltime
from cls import cls
import time
import json
schedule={}


def start():
    hotelsize, pause = chooseoption()
    if pause == 'start':
        return
    roommaker(hotelsize)
    hotelfolder = findfolder()
    with open(findfolder()+'\\'+'time.txt', 'w') as f:
        f.write('1')
        f.close()
    breakfastnum = {
        'breakf':0,
        'breakpers':0}
    with open(findfolder()+'\\'+'breakfastnum.json', 'w') as f:
        json.dump(breakfastnum, f, indent=4)
        f.close()

    with open(hotelfolder + '\\' + 'hoteldata.json', 'r') as f:
        hoteldata = json.loads(f.read())
        f.close()
    with open(hotelfolder + '\\' + 'schedule.json', 'w') as f:
        for x in range(100):
            cleantime = 2400+x*4800
            schedule.update({cleantime:'clean1'})
        json.dump(schedule,f, indent=4)
        f.close()
    totalrooms = (hoteldata['totalrooms'])
    totalcustomers = totalrooms * random.uniform(0.6,0.8)
    custdata = {}
    with open(hotelfolder + '\\' + 'custdata.json', 'w') as f:

        for _ in range(int(totalcustomers)):
            p, customer = reservation()
            print(customer)
            if p == 1:
                print('room unavb')

            elif customer['customername'] != "":
                customername = customer['customername']
                custdata[customername] = customer


        json.dump(custdata, f, indent=4)

        f.close()

    print('end')
    city = {'start':1}
    with open(findfolder()+'\\'+'city.json', 'w') as f:
        json.dump(city, f , indent=4)
        f.close()
    breakfast = {'start': 1}
    with open(findfolder() + '\\' + 'breakfast.json', 'w') as f:
        json.dump(breakfast, f, indent=4)
        f.close()
    restaurant = {'start': 1}
    with open(findfolder() + '\\' + 'restaurant.json', 'w') as f:
        json.dump(restaurant, f, indent=4)
        f.close()
    pool = {'start': 1}
    with open(findfolder() + '\\' + 'pool.json', 'w') as f:
        json.dump(pool, f, indent=4)
        f.close()
    return


def counter():
    start()
    hotelfolder = findfolder()
    with open(hotelfolder + '\\' + 'hoteldata.json', 'r') as f:
        hoteldata = json.loads(f.read())
        f.close()
    totalrooms = (hoteldata['totalrooms'])
    totalcustomers = totalrooms - (hoteldata['normalroomsavb'] + hoteldata['suitesavb'] + hoteldata['luxurysuitesavb'])
    persperit = totalcustomers/48000
    
    with open(findfolder()+'\\'+'time.txt', 'r') as f:
            count = int(f.read())
            f.close()

    with open(findfolder()+'\\'+'breakfastnum.json', 'r') as f:
        breakfastnum = json.loads(f.read())
        f.close()
    liveupdate = []
    breakf, breakpers=breakfastnum['breakf'], breakfastnum['breakpers']

    while True:
        randomnumber = random.uniform(0, 1)
        if randomnumber < persperit:

            with open(hotelfolder + '\\' + 'custdata.json', 'r') as f:
                custdata = json.loads(f.read())
                f.close()
            p, customer = reservation()
            if p == 1:
                liveupdate.insert(0,'there was no room available for '+customer)
            else:
                customername1 = customer['customername']
                custdata[customername1] = customer
                customername = customer['customername']
                customerroom = customer['stayingin']
                enterupdate = '{0} entered the hotel at {1} and checked in into room {2}'.format(customername, count,
                                                                                                 customerroom)
                liveupdate.insert(0,enterupdate)
                with open(hotelfolder + '\\' + 'custdata.json', 'w') as f:
                    json.dump(custdata, f, indent=4)
                    f.close()
        breakpers, breakf, daytime = breakfast(hoteltime(),breakf,totalcustomers, breakpers)

        actiontrue, action, name = custactions(hoteltime(), totalcustomers)
        if actiontrue == 'true':
            liveupdate.insert(0, action)
        if daytime == 1200:
            liveupdate.insert(0, 'the breakfast opens')
        elif daytime == 2200:
            liveupdate.insert(0, 'the breakfast closes')


        with open(findfolder()+'\\'+'schedule.json', 'r') as f:
            schedule = json.loads(f.read())

            if str(count) in schedule:

                if 'clean1' in schedule[str(count)]:
                    cleaners()
                    cleanupdate = 'the rooms were cleaned at {0}'.format(count)
                    liveupdate.insert(0,cleanupdate)

                elif schedule[str(count)].endswith(' checkout'):
                    personname = schedule[str(count)]
                    personname = personname[:-9]
                    checkout(personname)
                    checkoutupdate = '{0} checked out at {1}'.format(personname, count)
                    liveupdate.insert(0,checkoutupdate)
                else:
                    if schedule[str(count)].endswith(' rest'):
                        personname = schedule[str(count)]
                        personname = personname[:-5]
                    elif schedule[str(count)].endswith(' city'):
                        personname = schedule[str(count)]
                        personname = personname[:-5]
                    elif schedule[str(count)].endswith(' brea'):
                        personname = schedule[str(count)]
                        personname = personname[:-5]
                    elif schedule[str(count)].endswith(' pool'):
                        personname = schedule[str(count)]
                        personname = personname[:-5]
                    with open(findfolder() + '\\' + 'custdata.json', 'r') as f:
                        customersdata = json.loads(f.read())
                        f.close()
                    custdata = customersdata[personname]
                    custdata['status'] = 'inroom'
                    custdata['goesout'] = ''
                    customersdata[personname] = custdata
                    with open(findfolder() + '\\' + 'custdata.json', 'w') as f:
                        json.dump(customersdata, f, indent=4)
                        f.close()

        f.close()
        if (hoteltime() / (4800*7)).is_integer():
            money(369)
        if len(liveupdate) >= 11:
            lenliveupdate = len(liveupdate) - 10
            for _ in range(lenliveupdate):
                liveupdate.pop(10)
        time.sleep(0.02)

        if (count/300).is_integer() or count == 1:
            cls()

            with open(hotelfolder + '\\' + 'hoteldata.json', 'r') as f:
                hoteldata = json.loads(f.read())
                f.close()
                totalrooms, totalroomsavb, totalnormal, normalavb, totalsuite, suiteavb, totallux, luxavb, revenue, weekrevenue = hoteldata['totalrooms'], hoteldata['normalroomsavb'] + hoteldata['suitesavb'] + hoteldata['luxurysuitesavb'],hoteldata['normalrooms'],hoteldata['normalroomsavb'],hoteldata['suites'],hoteldata['suitesavb'],hoteldata['luxurysuites'],hoteldata['luxurysuitesavb'], hoteldata['revenue'], hoteldata['lastweekrev']
                livedata = ('''
                total rooms: {0}   total rooms available: {1}
                normal rooms: {2}  normal rooms available: {3}
                suites: {4}        suites available: {5}
                luxury suites: {6} luxury suites available: {7}
                total revenue: {8} last week's revenue: {9} '''.format(totalrooms, totalroomsavb, totalnormal,
                                                                          normalavb, totalsuite, suiteavb, totallux,
                                                                          luxavb, revenue, weekrevenue))

            print(livedata)
            lenliveupdate = len(liveupdate)
            if lenliveupdate > 10:
                size = lenliveupdate - (lenliveupdate - 10)
            else:
                size = lenliveupdate

            for x in range(size):

                print(liveupdate[x])
            liveupdate=[]


        count += 1
        breakfastnum['breakf'], breakfastnum['breakpers'] = breakf, breakpers
        with open(findfolder()+'\\'+'breakfastnum.json', 'w') as f:
            json.dump(breakfastnum, f, indent=4)
            f.close()

        with open(findfolder()+'\\'+'time.txt', 'w') as f:
            f.write(str(count))
            f.close()
counter()

