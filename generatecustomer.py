import random
import os
import json
from folderfinder import findfolder
import names
def gencustomer():


    customername = names.get_full_name()
    customernamewospace = customername.replace(' ', '')
    roomrandom = random.uniform(0,3)
    if roomrandom < 2:
        desiredroom = 'normal'
    elif roomrandom < 2.6:
        desiredroom = 'suite'
    else:
        desiredroom = 'luxury suite'


    return customernamewospace, customername, desiredroom
