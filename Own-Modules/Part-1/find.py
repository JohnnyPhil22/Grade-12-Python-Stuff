from findarea import *

opt='y'
while opt in 'yY':
    print("1. Area of square")
    print("2. Area of rectangle")
    print("3. Area of triangle")
    ch=int(input("Enter choice: "))
    if ch==1:
        s=int(input('Enter side: '))
        print('Area of square:',arsq(s))
    elif ch==2:
        l=int(input('Enter length: '))
        b=int(input('Enter breadth: '))
        print('Area of rectangle:',arrect(l,b))
    elif ch==3:
        b=int(input('Enter base: '))
        h=int(input('Enter height: '))
        print('Area of triangle:',artri(b,h))
    else:
        print('Select from options 1 to 3')
    opt=input('Press y to continue: ')
