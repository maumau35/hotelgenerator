import time
import json
import os
import random
import swimmingpooltemplates
import chooseoption
from folderfinder import findfolder


def swimmingpoolmaker(hotelsize):
    global jsonswimmingpooltemp

    if hotelsize.isnumeric:
        hotelsize=int(hotelsize)

        if hotelsize == 1:
            swimmingpoolsmin = 1

            multiplier = 1
            placesswimmingpool = 25
            name = 'small'

        if hotelsize == 2:
            swimmingpoolsmin = 2

            multiplier = 1.5
            placesswimmingpool = 30
            name = 'medium'


        if hotelsize == 3:

            swimmingpoolsmin = 3
            multiplier = 2
            placesswimmingpool = 40

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
        swimmingpools = swimmingpoolsmin + randomnumber
        currentswimmingpool = 0
        print(swimmingpools)
        swimmingpoolnumber = 1
        placesswimingpool = {}
        with open(findfolder()+ "//" + 'swimmingpoolfile.json', 'w') as f:
            while currentswimmingpool <= swimmingpools:
                for _ in range(placesswimmingpool):
                    stringswimmingpool = str(swimmingpoolnumber)
                    if len(stringswimmingpool) == 1:
                        stringswimmingpool = '0' + stringswimmingpool
                    swimmingpool = 'swimmingpool ' + str(currentswimmingpool) + stringswimmingpool


                    if swimmingpoolnumber == placesswimingpool:
                        swimmingpoolnumber = 1
                        currentswimmingpool += 1
                    else:
                        swimmingpoolnumber += 1
            json.dump(swimmingpools, f, indent=4)
            f.close()

        with open(cwd + "\\" + hoteldir + "\\" + 'hoteldata.json', "w") as f:
            hoteldatajson = {
                'totalplacesswimmingpool':(swimmingpools+1)*placesswimingpool,
                'swimmingpools':swimmingpools,
                'placesswimingpool':placesswimingpool,

            }
            json.dump(hoteldatajson, f)
            f.close()
        with open(cwd + "\\" + hoteldir + "\\" + 'time.txt', "w") as f:
            f.write('0')
            f.close()

    else:
        print('error, please enter a number')
        swimmingpoolmaker()
