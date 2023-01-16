# Input temperature and ask user whether to convert from Celsius to Fahrenheit or vice versa. Write functions and import here
from temp import *
opt='y'
while opt in 'yY':
    print('1. Celsius to Fahrenheit')
    print('2. Fahrenheit to Celsius')
    ch=int(input('Enter choice: '))
    if ch==1:
        c=eval(input('Enter temperature: '))
        ctof(c)
    elif ch==2:
        f=eval(input('Enter temperature: '))
        ftoc(f)
    else:
        print('Enter either 1 or 2')
    opt=input('Press y to continue: ')