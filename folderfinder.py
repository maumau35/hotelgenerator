import os
def findfolder():
    with open('lastchoice.txt', 'r') as f:
        hotelsize = f.read()
        f.close()

    if int(hotelsize) == 3:
        hotelsizename = 'big'
    elif int(hotelsize) == 2:
        hotelsizename = 'medium'
    else:
        hotelsizename = 'small'
    with open('hotelnumber' + hotelsizename + '.txt', 'r') as f:
        hotelnumber = int(f.read()) - 1
        f.close()
    cwd = os.getcwd()
    hotelfolder = cwd + '\\' + hotelsizename + str(hotelnumber)
    return hotelfolder
