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

# Write a menu driven program for tables stud(grno,name,dob,class,tcode,tcode2,fees) and teacher(tcode,tname,subject) to insert a record into stud or teacher table, delete a record either from stud or teacher table, increase the fees by 100 if student is in 12, display no of students in each class, display grno, sname, class, tcode, tname & subject for an inputted teacher code andd isplay names of students who are enrolled in Computer Science.
from mysql.connector import *

a=connect(host='localhost',user='root',password='Jp22')

cur=a.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS SCHOOL;')
cur.execute('USE SCHOOL;')

cur.execute('CREATE TABLE IF NOT EXISTS STUD (GRNO int(5), NAME varchar(25), DOB date, CLASS int(2), TCODE varchar(10), TCODE2 varchar(10), FEES float(8,2));')
cur.execute('DELETE FROM STUD;')

cur.execute('CREATE TABLE IF NOT EXISTS TEACHER (TCODE varchar(10), TNAME varchar(25), SUBJECT varchar(35));')
cur.execute('DELETE FROM TEACHER;')

a.commit()

opt='y'
if a.is_connected():
    print('Successfully Connected!')
    while opt in 'yY':
        print('1. Insert record to student or teacher table\n2. Delete record from student or teacher table\n3. Increase fees by 100 if student is in 12th\n4. Display number of students in each class\n5. Display GRNO, SNAME, CLASS, TCODE, TNAME and SUBJECT for inputted teacher code\n6. Display names of students enrolled in Computer Science\n7. Exit')
        ch=int(input('Enter choice: '))
        if ch==1:
            print('1. Input record to student table\n2. Input record to teacher table')
            table_choice=int(input('Enter choice: '))
            if table_choice==1:
                no_of_students=int(input('Enter number of students: '))
                for i in range(no_of_students):
                    grno=int(input('Enter GR Number: '))
                    name=input('Enter name: ')
                    dob=input('Enter date of birth (YYYY-MM-DD): ')
                    clas=int(input('Enter class: '))
                    tcode=input('Enter teacher code 1: ')
                    tcode2=input('Enter teacher code 2: ')
                    fees=float(input('Enter fees: '))
                    cur.execute("INSERT INTO STUD (GRNO,NAME,DOB,CLASS,TCODE,TCODE2,FEES) VALUES ({},'{}','{}',{},'{}','{}',{});".format(grno,name,dob,clas,tcode,tcode2,fees))

                cur.execute('SELECT * FROM STUD;')
                table=cur.fetchall()
                print('Final student table:')
                for r in table: print(r)

                a.commit()
            
            if table_choice==2:
                no_of_teachers=int(input('Enter number of teachers: '))
                for i in range(no_of_teachers):
                    tcode=input('Enter teacher code: ')
                    name=input('Enter name: ')
                    subject=input('Enter subject: ')
                    cur.execute("INSERT INTO TEACHER (TCODE,TNAME,SUBJECT) VALUES ('{}','{}','{}');".format(tcode,name,subject))

                cur.execute('SELECT * FROM TEACHER;')
                table=cur.fetchall()
                print('Final teacher table:')
                for r in table: print(r)

                a.commit()
                
            opt=input('Would you like to continue: ')
        if ch==2:
            print('1. Delete record from student table\n2. Delete record from teacher table')
            table_choice=int(input('Enter choice: '))
            if table_choice==1:
                GRNO_to_delete=int(input('Input GR number to delete data: '))
                cur.execute('DELETE FROM STUD WHERE GRNO={};'.format(GRNO_to_delete))
                
                a.commit()

            if table_choice==2:
                TCODE_to_delete=input('Enter teacher code to delete: ')
                cur.execute("DELETE FROM TEACHER WHERE TCODE='{}';".format(TCODE_to_delete))
                
                a.commit()

            opt=input('Would you like to continue: ')
        if ch==3:
            cur.execute('UPDATE STUD SET FEES = FEES + 100 WHERE CLASS=12;')
            cur.execute('SELECT * FROM STUD;')
            table=cur.fetchall()
            print('Final table:\n',table)

            a.commit()

            opt=input('Would you like to continue: ')
        if ch==4:
            cur.execute('SELECT CLASS,COUNT(CLASS) FROM STUD GROUP BY CLASS;')
            table=cur.fetchall()
            print('Final table:')
            for r in table: print(r)

            a.commit()

            opt=input('Would you like to continue: ')
        if ch==5:
            teacher_code_for_details=input('Enter teacher code for details: ')
            cur.execute("SELECT STUD.GRNO, STUD.NAME, STUD.CLASS, TEACHER.TCODE, TEACHER.TNAME, TEACHER.SUBJECT FROM STUD, TEACHER WHERE TEACHER.TCODE='{}' AND STUD.TCODE='{}' OR STUD.TCODE2='{}'".format(teacher_code_for_details,teacher_code_for_details,teacher_code_for_details))
            table=cur.fetchall()
            print('Final table:')
            for r in table: print(r)

            a.commit()

            opt=input('Would you like to continue: ')
        if ch==6:
            cur.execute("SELECT NAME FROM STUD, TEACHER WHERE TEACHER.SUBJECT='COMPUTER SCIENCE' and TEACHER.TCODE=STUD.TCODE;")
            table=cur.fetchall()
            print('Final table:')
            for r in table: print(r)

            a.commit()

            opt=input('Would you like to continue: ')
        if ch==7:
            opt='n'