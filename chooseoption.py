
def chooseoption():
    hotelsize = input("""

    please select your hotel size by choosing a number
    1 small
    2 medium
    3 big
    """)
    with open('lastchoice.txt', 'w') as f:
        f.write(hotelsize)
        f.close()
    return hotelsize