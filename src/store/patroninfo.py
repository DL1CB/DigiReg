
"""
This stores the patroninfo state of the device
"""

patroninfo = {
    "date":324329874298, 
    "name":"Kellerstrasse 16 ",
    "phone":"+4917370702569",
    "email":"chris.bentley@wireup.io"
}

# mutations
def date( *argv ):
    if len(argv):
        patroninfo["date"] = argv[0]
    return patroninfo["date"]

def name( *argv ):
    if len(argv):
        patroninfo["name"] = argv[0]
    return patroninfo["name"]

def phone( *argv ):
    if len(argv):
        patroninfo["phone"] = argv[0]
    return patroninfo["phone"]

def email( *argv ):
    if len(argv):
        patroninfo["email"] = argv[0]
    return patroninfo["email"]        

#actions
def save( filename='patroninfo.json' ):
    """write patroninfo to flash"""
    import json
    with open(filename, 'w') as file:
        json.dump(patroninfo, file)

def load( filename='patroninfo.json' ):
    """load patroninfo from flash"""
    import json 
    try:
        with open(filename, 'r') as file:
            global patroninfo
            patroninfo = json.load(file)
    except Exception :
        pass

