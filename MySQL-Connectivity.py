# Create menu driven program for table ITEM with attributes ITNO, ITName, Price, Discount to Insert, Update discount & Make discount 0
from mysql.connector import *

a=connect(host='localhost',user='root',password='Jp22')

cur=a.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS ITEMDATABASE;')
cur.execute('USE ITEMDATABASE;')
cur.execute('CREATE TABLE IF NOT EXISTS ITEM (ITNO int(15), ITName varchar(25), Price float(15,2), DISCOUNT int(5));')
cur.execute('DELETE FROM ITEM;')

opt='y'
if a.is_connected():
    print('Successfully Connected!')
    while opt in 'yY':
        print('1. Insert record\n2. Update discount for item\n3. Change discount for items starting with P\n4. Exit')
        ch=int(input('Enter choice: '))
        if ch==1:
            itno=int(input('Enter item number: '))
            itname=input('Enter item name: ')
            price=float(input('Enter price: '))
            discount=int(input('Enter discount: '))
            cur.execute("INSERT INTO ITEM (ITNO,ITName,Price,DISCOUNT) VALUES ({},'{}',{},{});".format(itno,itname,price,discount))

            cur.execute('SELECT * FROM ITEM;')
            table=cur.fetchall()
            print('Final table:')
            for r in table: print(r)

            a.commit()

            opt=input('Would you like to continue: ')
        if ch==2:
            itname=input('Enter item name: ')
            cur.execute("UPDATE ITEM SET DISCOUNT = DISCOUNT + 2 WHERE ITName='{}';".format(itname))

            cur.execute('SELECT * FROM ITEM;')
            table=cur.fetchall()
            print('Final table:')
            for r in table: print(r)

            a.commit()

            opt=input('Would you like to continue: ')
        if ch==3:
            cur.execute("UPDATE ITEM SET DISCOUNT = 0 WHERE ITName LIKE 'P%'")

            cur.execute('SELECT * FROM ITEM;')
            table=cur.fetchall()
            print('Final table:')
            for r in table: print(r)

            a.commit()

            opt=input('Would you like to continue: ')
        if ch==4:
            opt='n'