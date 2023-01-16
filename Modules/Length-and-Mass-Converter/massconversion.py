kgtonne=0.001
kgpound=2.20462

def help():
    print('2 converts weight entered in kilograms to tonnes\n3 converts weight entered in tonnes to kilograms\n4 converts weight entered in kilogram to pounds\n5 converts weight entered in pounds to kilograms')

def kg_to_tonne(n):
    return n*kgtonne

def tonne_to_kg(n):
    return n/kgtonne

def kg_to_pound(n):
    return n*kgpound

def pound_to_kg(n):
    return n/kgpound