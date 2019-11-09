import os
import time
import random

def getIdOfRoom():
    idOfRoom = 'pictures/' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '_' + str(random.randint(100, 999))
    os.makedirs(idOfRoom, exist_ok=True)
    return idOfRoom
