
def chooseoption():
    hotelsize = input("""

    please select your hotel size by choosing a number
    1 small
    2 medium
    3 big
    or if you would like to continue your last hotel type 'start'

    """)
    print(hotelsize)

    if hotelsize == 'start':
        hotelsize = input("""

    please select your hotel size by choosing a number
    1 small
    2 medium
    3 big

    """)
        pause = 'start'
    else:
        pause = 'x'
    with open('lastchoice.txt', 'w') as f:
            f.write(hotelsize)
            f.close()
    return hotelsize, pause
