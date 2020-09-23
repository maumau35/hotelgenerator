import json
import time
from folderfinder import findfolder
import random
def pool(time1, name):
    with open(findfolder()+'\\'+'pool.json', 'r') as f:
        pool = json.loads(f.read())
        f.close()
    options = ['lying on a bed', 'swimming in the pool']
    choice = random.choice(options)

    with open(findfolder() +'\\' + 'custdata.json', 'r') as f:
        customersdata = json.loads(f.read())
        f.close()
    with open(findfolder() +'\\' + 'schedule.json', 'r') as f:
        schedule = json.loads(f.read())
        f.close()
    custdata = customersdata[name]
    localtime = int(int(time1) / 4800 - 0.5)
    time1 = int(time1) - localtime * 4800
    time = time1 + random.randint(100, 300)
    for _ in range(10000):
        if time not in schedule:
            break
        else:
            time = int(random.uniform(200, 400) + time1)

    custdata['status'] = choice
    schedule.update({time: name + ' pool'})
    custdata['goesout'] = time

    pool.update({name: choice})
    with open(findfolder() + '\\' + 'pool.json', 'w') as f:
        json.dump(pool, f, indent=4)
        f.close()
    customersdata[name] = custdata


    with open(findfolder() + '\\' + 'schedule.json', 'w') as f:
        json.dump(schedule, f, indent=4)
        f.close()
    with open(findfolder() + '\\' + 'custdata.json', 'w') as f:
        json.dump(customersdata, f, indent=4)
        f.close()