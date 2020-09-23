from folderfinder import findfolder
def hoteltime():
    with open(findfolder()+'\\'+'time.txt', 'r') as f:
        time1 = int(f.read())
        f.close()
    return time1
