from lengthconversion import *
from massconversion import *

opt='y'
while opt in 'yY':
    print('1. Convert lengths\n2. Convert mass')
    ch=int(input('Enter choice: '))
    if ch==1:
        opt1='y'
        while opt1 in 'yY':
            print('1. Help\n2. Convert mile to kilometer\n3. Convert kilometer to mile\n4. Convert feet to inches\n5. Convert inches to feet')
            ch1=int(input('Enter choice: '))
            if ch1==1:
                help()
            elif ch1==2:
                n=eval(input('Enter length in miles: '))
                print('It is equal to',mile_to_km(n),'kilometers')
            elif ch1==3:
                n=eval(input('Enter length in kilometer: '))
                print('It is equal to',km_to_mile(n),'miles')
            elif ch1==4:
                n=eval(input('Enter length in feet: '))
                print('It is equal to',feet_to_inches(n),'inches')
            elif ch1==5:
                n=eval(input('Enter length in inches: '))
                print('It is equal to',inches_to_feet(n),'feet')
            else:
                print('Select from options 1 through 5')
            opt1=input('Press y to continue: ')
        if opt1!='y' or opt1!='Y':
            break
    elif ch==2:
        opt2='y'
        while opt2 in 'yY':
            print('1. Help\n2. Convert kilograms to tonnes\n3. Convert tonnes to kilograms\n4. Convert kilograms to pounds\n5. Convert pounds to kilograms')
            ch2=int(input('Enter choice: '))
            if ch2==1:
                help()
            elif ch2==2:
                n=eval(input('Enter weight in kilograms: '))
                print('It is equal to',kg_to_tonne(n),'tonnes')
            elif ch2==3:
                n=eval(input('Enter weight in tonnes: '))
                print('It is equal to',tonne_to_kg(n),'kilograms')
            elif ch2==4:
                n=eval(input('Enter weight in kilograms: '))
                print('It is equal to',kg_to_pound(n),'pounds')
            elif ch2==5:
                n=eval(input('Enter weight in pounds: '))
                print('It is equal to',pound_to_kg(n),'kilograms')
            else:
                print('Select from options 1 through 5')
            opt2=input('Press y to continue: ')
        if opt2!='y' or opt2!='Y':
            break
    else:
        print('Select either 1 or 2')
    opt=input('Press y to continue: ')