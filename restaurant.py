import json
import time
from folderfinder import findfolder
import random
from money import money
def restaurant(time1, name):
    with open(findfolder()+'\\'+'restaurant.json', 'r') as f:
        restaurant = json.loads(f.read())
        f.close()
    options = ['steak', 'burger', 'carpaccio', 'spaghetti bolognese']
    choice = random.choice(options)

    with open(findfolder() +'\\' + 'custdata.json', 'r') as f:
        customersdata = json.loads(f.read())
        f.close()

    with open(findfolder() +'\\' + 'schedule.json', 'r') as f:
        schedule = json.loads(f.read())
        f.close()
    custdata = customersdata[name]
    time = int(time1) + random.randint(200, 400)
    for _ in range(10000):
        if time not in schedule:
            break
        else:
            time1 = int(random.uniform(200, 400) + time1)
    custdata['status'] = 'dining in the hotel'
    custdata['lastate'] = choice
    schedule.update({time: name + ' rest'})
    custdata['goesout'] = time
    customersdata[name] = custdata
    restaurant.update({name: choice})
    with open(findfolder() + '\\' + 'restaurant.json', 'w') as f:
        json.dump(restaurant, f, indent=4)
        f.close()
    customersdata[name] = custdata
    money(30)


    with open(findfolder() + '\\' + 'schedule.json', 'w') as f:
        json.dump(schedule, f, indent=4)
        f.close()
    with open(findfolder() + '\\' + 'custdata.json', 'w') as f:
        json.dump(customersdata, f, indent=4)
        f.close()