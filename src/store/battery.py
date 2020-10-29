from drivers.i2c import i2c
from drivers.ip5306 import IP5306

battery = IP5306(i2c)

"""
This stores the battery sate of the device
"""
#getters
def batterylevel():
    """ int persentage of the battery level in descrete steps 0, 25, 50, 75, 100 """
    return battery.level

def batterycharging():
    """ bool if charging or not """
    return battery.charging

def batteryfull():
    """ bool if charged or not """
    return battery.full    


