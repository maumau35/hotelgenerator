from folderfinder import findfolder
import json
from hoteltime import hoteltime
def money(money):
    with open(findfolder() + '\\' + 'hoteldata.json', 'r') as f:
        hoteldata = json.loads(f.read())
        f.close()
    if money == 369:
        lastweekrev = hoteldata['curweekrev']
        hoteldata['lastweekrev'] = lastweekrev
        hoteldata['curweekrev'] = 0
    else:
        if hoteltime() > 1:
            wrevenue = hoteldata['curweekrev']
            wrevenue += money
            hoteldata['curweekrev'] = wrevenue
        revenue = hoteldata['revenue']
        revenue += money
        hoteldata['revenue'] = revenue


    with open(findfolder() + '\\' + 'hoteldata.json', 'w') as f:
        json.dump(hoteldata, f, indent=4)
        f.close()