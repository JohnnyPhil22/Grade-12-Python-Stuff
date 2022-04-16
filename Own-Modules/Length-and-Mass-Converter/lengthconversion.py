mile=1.609344
feet=12

def help():
    print('2 converts length entered in miles to kilometers\n3 converts length entered in kilometers to miles\n4 converts length entered in feet to inches\n5 converts length entered in inches to feet')

def mile_to_km(n):
    return n*mile

def km_to_mile(n):
    return n/mile

def feet_to_inches(n):
    return n*feet

def inches_to_feet(n):
    return n/feet
