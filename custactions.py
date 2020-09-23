from roomgen import roommaker
from chooseoption import chooseoption
from folderfinder import findfolder
from reservation import reservation
from cleaners import cleaners
from checkout import checkout
from restaurant import restaurant
from swimmingpool import pool
from city import goingcity
import random
from cls import cls
import time
import json

def custactions(time1, totalcustomers):


    localtime = int(time1 / 4800 - 0.5)
    daytime = time1 - localtime * 4800
    chanceforaction = totalcustomers / 1000
    if chanceforaction > random.uniform(0, 1):
        with open(findfolder() + '\\' + 'custdata.json', 'r') as f:
            custdataactions = json.loads(f.read())
            f.close()
        customerlist = [*custdataactions]



        customer = random.choice(customerlist)
        chancerestaurant = random.uniform(0,1)
        chanpoolcit = random.uniform(0,1)
        customer1 = custdataactions[customer]

        if daytime > 600 and daytime < 1200 or custdataactions[customer]['status'] != 'inroom' or (time1+800)> customer1['checksout']:
            return 'false', 'x', 'y'
        elif daytime > 3200 and daytime < 4400 and chancerestaurant < 0.8:
            restaurant(time1, customer)
            return 'true', customer + ' is going to the restaurant', customer
        elif chanpoolcit < 0.3:
            pool(time1, customer)
            return 'true', customer + ' is going to the pool', customer
        else:
            activity = goingcity(time1, customer)
            return 'true', customer+activity , customer
    else:
        return 'false', 'x', 'y'


