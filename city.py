import json
import time
from folderfinder import findfolder
import random
def goingcity(time, name):
    with open(findfolder()+'\\'+'city.json', 'r') as f:
        city = json.loads(f.read())
        f.close()
    todolistevening = [' is at a bar in the city', ' is dining in a restaurant in the city', ' is partying in a club']
    todolistmorning = [' is dining in a restaurant in the city', ' is sightseeing', ' is attending a meeting', ' is doing business']

    with open(findfolder() + '\\' + 'custdata.json', 'r') as f:
        customersdata = json.loads(f.read())
        f.close()
    custdata = customersdata[name]

    with open(findfolder() +'\\' + 'schedule.json', 'r') as f:
        schedule = json.loads(f.read())
        f.close()

    localtime = int(time/4800-0.5)
    time1 = time - localtime*4800
    if time1 < 1200 or time1 > 3400:
        activity = random.choice(todolistevening)
    else:
        activity = random.choice(todolistmorning)

    custdata['status'] = activity
    until = time+random.randint(100, 600)
    for _ in range(10000):
        if until not in schedule:
            break
        else:
            until = int(random.uniform(100, 600) + time)
    schedule.update({until: name + ' city'})
    custdata['goesout'] = until

    city.update({name: activity + ' until ' + str(until)})
    with open(findfolder() + '\\' + 'city.json', 'w') as f:
        json.dump(city, f, indent=4)
        f.close()
    customersdata[name] = custdata


    with open(findfolder() + '\\' + 'schedule.json', 'w') as f:
        json.dump(schedule, f, indent=4)
        f.close()
    with open(findfolder() + '\\' + 'custdata.json', 'w') as f:
        json.dump(customersdata, f, indent=4)
        f.close()
    return activity
