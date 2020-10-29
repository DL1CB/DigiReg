"""
This stores the wifi state of the device
"""

wifistate = {
    "ssid":"SpringTime", 
    "password":"Calmhat436",
}

# mutations
def ssid( *argv ):
    if len(argv):
        wifistate["ssid"] = argv[0]
    return wifistate["ssid"]

def password( *argv ):
    if len(argv):
        wifistate["password"] = argv[0]
    return wifistate["password"]

#actions
def save( filename='wifistore.json' ):
    """write wifistate to flash"""
    import json
    with open(filename, 'w') as file:
        json.dump(wifistate, file)

def load( filename='wifistore.json' ):
    """load wifistate from flash"""
    import json 
    try:
        with open(filename, 'r') as file:
            global wifistate
            wifistate = json.load(file)
    except Exception :
        pass

load() # the wifistate set from flash, when the library is first called