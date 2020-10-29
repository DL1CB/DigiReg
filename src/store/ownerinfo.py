
"""
This stores the ownerinfo state of the device
"""

ownerinfo = {
    "name":"Pizza Napoli", 
    "street":"Kellerstrasse 16",
    "city":"Gremsdorf",
    "zip":"91350",
    "state":"Bayern",
    "country":"Germany",
    "phone":"+4917370702569",
    "email":"chris.bentley@wireup.io"
}

# mutations
def name( *argv ):
    if len(argv):
        ownerinfo["name"] = argv[0]
    return ownerinfo["name"]

def street( *argv ):
    if len(argv):
        ownerinfo["street"] = argv[0]
    return ownerinfo["street"]

def city( *argv ):
    if len(argv):
        ownerinfo["city"] = argv[0]
    return ownerinfo["city"]

def zip( *argv ):
    if len(argv):
        ownerinfo["zip"] = argv[0]
    return ownerinfo["zip"]

def state( *argv ):
    if len(argv):
        ownerinfo["state"] = argv[0]
    return ownerinfo["state"]

def country( *argv ):
    if len(argv):
        ownerinfo["country"] = argv[0]
    return ownerinfo["country"]

def phone( *argv ):
    if len(argv):
        ownerinfo["phone"] = argv[0]
    return ownerinfo["phone"]

def email( *argv ):
    if len(argv):
        ownerinfo["email"] = argv[0]
    return ownerinfo["email"]        



#actions
def save( filename='ownerinfo.json' ):
    """write ownerinfo to flash"""
    import json
    with open(filename, 'w') as file:
        json.dump(ownerinfo, file)

def load( filename='ownerinfo.json' ):
    """load ownerinfo from flash"""
    import json 
    try:
        with open(filename, 'r') as file:
            global ownerinfo
            ownerinfo = json.load(file)
    except Exception :
        pass

load() # the ownerinfo set from flash, when the library is first called