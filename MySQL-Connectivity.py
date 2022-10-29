'''
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
'''
# Create menu driven program for table ITEM with attributes ITCode, ITName, Price, Discount to Display item code and item name of those items starting with P, Display details in descending order of price, Print n number of records & Print records if price between 40 and 45
from mysql.connector import *

a=connect(host='localhost',user='root',password='Jp22')

cur=a.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS ITEMDATABASE;')
cur.execute('USE ITEMDATABASE;')
cur.execute('CREATE TABLE IF NOT EXISTS ITEM_2 (ITCode varchar(15), ITName varchar(25), Price float(15,2), DISCOUNT int(5));')
cur.execute('DELETE FROM ITEM_2;')

no_of_items=int(input('Enter number of items to insert to table: '))
for i in range(no_of_items):
    itcode=input('Enter item code: ')
    itname=input('Enter item name: ')
    price=float(input('Enter price: '))
    discount=int(input('Enter discount: '))
    cur.execute("INSERT INTO ITEM_2 (ITCode,ITName,Price,DISCOUNT) VALUES ('{}','{}',{},{});".format(itcode,itname,price,discount))

cur.execute('SELECT * FROM ITEM_2;')
table=cur.fetchall()
print('Final table:')
for r in table: print(r)

a.commit()

opt='y'
if a.is_connected():
    print('Successfully Connected!')
    while opt in 'yY':
        print('1. Display item code and item name if item name starts with P\n2. Display item details in descending order of price\n3. Print \'n\' number of records\n4. Fetch each record and print if price between 40 and 45\n5. Exit')
        ch=int(input('Enter choice: '))
        if ch==1:
            cur.execute("SELECT ITCode, ITName FROM ITEM_2 WHERE ITName LIKE 'P%';")
            table=cur.fetchall()
            print('Final table:')
            for r in table: print(r)

            a.commit()

            opt=input('Would you like to continue: ')
        if ch==2:
            cur.execute('SELECT * FROM ITEM_2 ORDER BY PRICE DESC;')
            table=cur.fetchall()
            print('Final table:')
            for r in table: print(r)

            a.commit()

            opt=input('Would you like to continue: ')
        if ch==3:
            n=int(input('Enter number of records to be printed: '))
            cur.execute('SELECT * FROM ITEM_2 LIMIT {};'.format(n))
            table=cur.fetchall()
            print('Final table:\n',table)

            a.commit()

            opt=input('Would you like to continue: ')
        if ch==4:
            cur.execute('SELECT * FROM ITEM_2 WHERE PRICE BETWEEN 40 AND 45;')
            table=cur.fetchall()
            print('Final table:')
            for r in table: print(r)

            a.commit()

            opt=input('Would you like to continue: ')
        if ch==5:
            opt='n'