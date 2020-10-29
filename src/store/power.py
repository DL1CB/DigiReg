"""
This stores the wakestate of the device for the sleep 
"""


def saveWakestate( wakestate, filename='wakestate.dat' ):
    """write wake state to flash"""
    import json
    with open(filename, 'w') as file:
        json.dump(wakestate, file)

def loadWakestate( filename='wakestate.dat' ):
    """load wake state from flash"""
    import json 
    try:
        with open(filename, 'r') as file:
            wakestate = json.load(file)
            print("loadWakestate",wakestate)
            return wakestate
    except Exception :
        return "welcome"