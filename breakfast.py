import json
import time
from folderfinder import findfolder
import random
from money import money
def breakfast(time1, breakf, totalcustomers, breakpers):
    localtime = int(time1 / 4800 - 0.5)
    daytime = time1 - localtime * 4800

    if daytime > 1200 and daytime < 2200:
        itpercus = int(900/totalcustomers)
        if itpercus != breakf:
            breakf += 1
            return breakpers, breakf, daytime
        elif breakf == itpercus:
            breakf = 0
            with open(findfolder() + '\\' + 'custdata.json', 'r') as f:
                customersdata = json.loads(f.read())
                f.close()

            customerlist = [*customersdata]
            maxlen = len(customerlist)
            if breakpers == maxlen:
                return breakpers, breakf, daytime
            name = customerlist[breakpers]

            breakpers += 1
            custdata = customersdata[name]

            if custdata['status'] == 'inroom' and (time1+300)< custdata['checksout']:
                with open(findfolder() + '\\' + 'breakfast.json', 'r') as f:
                    breakfast = json.loads(f.read())
                    f.close()
                options = ['croissant', 'yoghurt', 'smoked salmon', 'cake']
                choice = random.choice(options)

                with open(findfolder() + '\\' + 'schedule.json', 'r') as f:
                    schedule = json.loads(f.read())
                    f.close()

                time = time1 + random.randint(80, 300)
                for _ in range(10000):
                    if time not in schedule:
                        break
                    else:
                        time = int(random.uniform(100, 300) + time1)
                custdata['status'] = 'having breakfast'
                custdata['lastate'] = choice
                schedule.update({time: name + ' brea'})
                custdata['goesout'] = time
                customersdata[name] = custdata
                breakfast.update({name: choice})
                with open(findfolder() + '\\' + 'breakfast.json', 'w') as f:
                    json.dump(breakfast, f, indent=4)
                    f.close()
                customersdata[name] = custdata

                with open(findfolder() + '\\' + 'schedule.json', 'w') as f:
                    json.dump(schedule, f, indent=4)
                    f.close()
                with open(findfolder() + '\\' + 'custdata.json', 'w') as f:
                    json.dump(customersdata, f, indent=4)
                    f.close()
                    money(20)
                    return breakpers, breakf, daytime
            else:
                return breakpers, breakf, daytime
    else:
        return breakpers, breakf, daytime


