# Calculate sum of salaries and counting number of employees getting more than 7000
import csv
with open('employee.csv','r') as f:
    content,count,sum=csv.reader(f),0,0
    for r in content:
        sum+=int(r[2])
        if int(r[2])>7000:
            count+=1
print('Sum of salaries:',sum)
print('Number of employees with salary greater than 7000:',count)

# Create csv file and store employee number, name and salary. Search any employee number and display name and salary and if not found display apprporiate message.
import csv
with open('employee.csv','w') as f:
    filewrite=csv.writer(f)
    ans='y'
    while ans in 'yY':
        emplist=eval(input('Enter employee details (Format = [empno,empname,salary]): '))
        filewrite.writerow(emplist)
        ans=input('Do you wish to enter more: ')
ans='y'
with open('employee.csv','r') as f:
    fileread=csv.reader(f)
    while ans in 'yY':
        f,empnosrch=False,int(input('Enter employee number: '))
        for r in fileread:
            if len(r)!=0:
                if int(r[0])==empnosrch:
                    print('Employee name:',r[1])
                    print('Employee salary:',r[2])
                    f=True
                    break
        if not f:
            print('Employee not found')

# Create csv file book.csv with fields bno, bname, type and price. Delete records where type='fiction' from original file and put in new file fiction.csv.
import csv
with open('book.csv','w') as f:
    n=int(input('Enter number of books: '))
    for i in range(n):
        bno=int(input('Enter book number: '))
        bname=input('Enter book name: ')
        t=input('Enter book genre: ')
        price=float(input('Enter book price: '))
        f.write(str(bno)+','+bname+','+t+','+str(price)+'\n')
l=[]
with open('book.csv','r+') as f:
    fileread=csv.reader(f)
    for row in fileread:
        l.append(row)
        for i in range(len(l)):
            if l[i][2] in 'FICTIONfiction':
                with open('fiction.csv','a') as fnew:
                    csv.writer(fnew).writerow(l[i])
                del l[i]
with open('book.csv','w') as f:
    csv.writer(f).writerows(l)

# Get item details (code, description and price) for multiple items from the user and create a csv file by writing all the item details in one go.
import csv
d={}
with open('details.csv','w') as f:
    n=int(input('Enter number of items: '))
    for i in range(n):
        code=eval(input('Enter item code: '))
        desc=input('Enter item description: ')
        price=float(input('Enter item price: '))
        d[code,desc,price]=i
    csv.writer(f).writerows(d)
with open('details.csv','r',newline='\n') as f:
    fileread=csv.reader(f)
    for r in fileread:
        print(r)

# Write multiple rows together in one go and print file content
import csv
with open('result.csv','w') as f:
    filewrite=csv.writer(f)
    content=[['name','marks','grade'],['s',23,'A'],['t',24,'A'],['u',25,'A'],['b',26,'A']]
    filewrite.writerows(content)
with open('result.csv','r',newline='\n') as f:
    fileread=csv.reader(f)
    for r in fileread:
        print(r)

# Print employee details who have salary more than 4000
import csv
def dispemp():
    with open('file.csv','r',newline='\n') as f:
        fileread=csv.reader(f)
        for row in fileread:
            if int(row[2])>=4000:
                print(row)

# Print employee details for those whose names start with 'S' and print total number of people with names as such
import csv
def snames():
    with open('emp.csv','r',newline='\n') as f:
        count,fileread=0,csv.reader(f)
        for row in fileread:
            if row[1][0]=='S':
                count+=1
                print(row)
        print('Number of \'S\' names are',count,'/',len(fileread))

# Copy file contents to new file
import csv
def csvcopy(f,fnew):
    with open('file.csv','r') as f:
        with open('newfile.csv','w') as fnew:
            csv.writer(fnew).writerows(csv.writer(f))

# Menu driven program to keep inventory of toys [KEEP CREATE() OUTSIDE THE MENU, SO TO AVOID ACCIDENTAL OVERWRITING OF FILE, KEEP THE REST IN THE MENU.]
## CREATE() : TO CREATE A “TOY.CSV” FILE CONTAINING RECORDS HAVING THE FOLLOWING DETAILS: 
### NAME OF TOY 
### PRICE 
### CATEGORY 
### STK
### WRITE ALL THESE DETAILS FOR EVERY RECORD INTO THE FILE
import csv
def create():
    with open('toy.csv','w',newline='\r\n') as f:
        n=int(input("Enter the number of entries: "))
        for i in range(n):
            name=input("Enter toy name: ")
            price=int(input("Enter toy price: "))
            category=input("Enter toy category: ")
            stock=int(input("Enter toy stock: "))
            csv.writer(f).writerow([name,price,category,stock])

## DISPLAY(): TO DISPLAY THE CONTENTS OF THE FILE WHOSE FILE NAME IS INPUT BY THE USER 
def display():
    with open('toy.csv','r',newline='\r\n') as f:
        for i in csv.reader(f):
            print(i)

## SEARCH(): TO SEARCH AND DISPLAY FOR GIVEN NAME AS INPUT BY THE USER , GIVE APPROPRIATE MESSAGE IF RECORD NOT FOUND. 
def search():
    nametosrch=input("Enter toy name: ")
    with open('toy.csv','r',newline='\r\n') as f:
        for i in csv.reader(f):
            if i[0]==nametosrch:
                print(i)

## APPEND() : TO ADD ADDITIONAL ‘N’ RECORDS INTO “TOY.CSV” 
def append():
    with open('toy.csv','a',newline='\r\n') as f:
        n=int(input("Enter the number of entries: "))
        for i in range(n):
            name=input("Enter toy name: ")
            price=int(input("Enter toy price: "))
            category=input("Enter toy category: ")
            stock=int(input("Enter toy stock: "))
            csv.writer(f).writerow([name,price,category,stock])
    print('Updated contents of file:')
    display()

## HIGHEST(): TO COPY THE RECORDS OF TOYS WHERE PRICE > 100 INTO ANOTHER FILE CALLED “HIGHEST.CSV” 
def highest():
    with open('toy.csv','r',newline='\r\n') as f:
        l=[]
        for i in csv.reader(f):
            if int(i[1])>100:
                l.append(i)
    with open('highest.csv','a',newline='\r\n') as fnew:
        csv.writer(fnew).writerows(l)
    print('Contents of original file:')
    display()
    print('Contents of \'highest.csv\' file:')
    with open('highest.csv','r',newline='\r\n') as fnew:
        for i in csv.reader(fnew):
            print(i)

## MODIFY() : TO MODIFY STK OF THOSE TOYS WHERE STK IS LESS THAN 10 ,BY ADDING 10 TO THEIR EXISTING STK. 
def modify():
    with open('toy.csv','r',newline='\r\n') as f:
        l=[]
        for i in csv.reader(f):
            if int(i[3])<10:
                i[3]=int(i[3])+10
            l.append(i)
    with open('toy.csv','w',newline='\r\n') as f:
        csv.writer(f).writerows(l)
    display()

## DELETE(): TO DELETE ALL TOYS WHERE CATEGORY IS “FUN”.
###       NAME       PRICE CATEGORY STK
### BUILDING BLOCKS   45     EDU     34
### LEARNING SCIENCE  156   JUNIOR   5
### CAR               134    FUN     56
### ABACUS            78     EDU     12
### REMOTE DRONE      200    FUN     7
### BIKE              80    JUNIOR   28
def delete():
    with open('toy.csv','r',newline='\r\n') as f:
        l=[]
        for i in csv.reader(f):
            if i[2].lower()!='fun':
                l.append(i)
    with open('toy.csv','w',newline='\r\n') as f:
        csv.writer(f).writerows(l)
    display()

create()
opt='y'
while opt in 'yY':
    print('1. Display\n2. Search Name\n3. Append\n4. Highest\n5. Modify\n6. Delete')
    ch=int(input("Enter your choice: "))
    if ch==1:
        display()
    if ch==2:
        search()
    if ch==3:
        append()
    if ch==4:
        highest()
    if ch==5:
        modify()
    if ch==6:
        delete()
    if 0<ch>6:
        print('Please enter a number between 1 and 6')
    opt=input('Do you wish to continue: ')

# To create a menu driven program to manage student marks
## CREATE() : TO CREATE A “STUDENT.CSV” FILE CONTAINING N RECORDS HAVING THE FOLLOWING DETAILS : 
### NAME 
### ENGLISH MARKS 
### CSC MARKS 
### MATH MARKS 
### PHY MARKS
### CHEM MARKS 
### AVERAGE ( TO FIND AVERAGE FOR 5 SUBJECTS AND WRITE IT INTO FILE )
### WRITE ALL THESE DETAILS FOR EVERY RECORD INTO THE FILE –
import csv
def create():
    n=int(input("Enter the number of entries: "))
    with open('student.csv','w',newline='\n') as f:
        for i in range(n):
            name=input("Enter name: ")
            phy=int(input("Enter Physics marks: "))
            chem=int(input("Enter Chemistry marks: "))
            math=int(input("Enter Math marks: "))
            comp=int(input("Enter Computers marks: "))
            eng=int(input("Enter English marks: "))
            csv.writer(f).writerow([name,phy,chem,math,comp,eng,((phy+chem+math+comp+eng)/5)])

## DISPLAY(): TO DISPLAY THE CONTENTS OF THE FILE WHOSE FILE NAME IS INPUT BY THE USER IN A TABULAR FORM.
def display():
    with open('student.csv','r',newline='\r\n') as f:
        for i in csv.reader(f):
            print(i)

## SEARCH(): TO SEARCH AND DISPLAY FOR GIVEN NAME AS INPUT BY THE USER , GIVE APPROPRIATE MESSAGE IF RECORD NOT FOUND.
def search():
    q=input("Enter name: ")
    with open('student.csv','r',newline='\r\n') as f:
        for i in csv.reader(f):
            if i[0]==q:
                print(i)

## APPEND() : TO ADD ADDITIONAL ‘N’ RECORDS INTO “STUDENT.CSV” 
def append():
    n=int(input("Enter the number of entries: "))
    with open('student.csv','a',newline='\n') as f:
        for i in range(n):
            name=input("Enter name: ")
            phy=int(input("Enter Physics marks: "))
            chem=int(input("Enter Chemistry marks: "))
            math=int(input("Enter Math marks: "))
            comp=int(input("Enter Computers marks: "))
            eng=int(input("Enter English marks: "))
            csv.writer(f).writerow([name,phy,chem,math,comp,eng,((phy+chem+math+comp+eng)/5)])
    display()

## FAILURE(): TO COPY THE NAMES OF STUDENTS WHO HAVE FAILED EVEN IN ONE SUBJECT INTO ANOTHER FILE CALLED “FAIL.TXT”.
def failure():
    with open('student.csv','r',newline='\r\n') as f:
        l=[]
        for i in csv.reader(f):
            for j in range(1,6):
                if int(i[j])<34:
                    l.append(i)
                    break
    print('Contents of original file:')
    display()
    with open('fail.csv','a',newline='\r\n') as fnew:
        csv.writer(fnew).writerows(l)
    print('Contents of new file: ')
    with open('fail.csv','r',newline='\r\n') as fnew:
        for i in csv.reader(fnew):
            print(i)

## HIGHEST(): TO COPY THE RECORDS OF STUDENTS WHOSE AVERAGE IS GREATER THAN 85% INTO ANOTHER FILE CALLED “HIGHEST.CSV” 
def highest():
    with open('student.csv','r',newline='\r\n') as f:
        l=[]
        for i in csv.reader(f):
            if float(i[6])>85:
                l.append(i)
    with open('highest.csv','w',newline='\r\n') as fnew:
        csv.writer(fnew).writerows(l)
    print('Contents of original file:')
    display()
    print('Contents of new file:')
    with open('highest.csv','r',newline='\r\n') as fnew:
        for i in csv.reader(fnew):
            print(i)

## MODIFY() : TO MODIFY MARKS IN CSC OF THOSE STUDENTS WHO HAVE SCORED LESS THAN 50 , BY ADDING 10 TO THEIR MARKS , THE CHANGE MUST BE EVIDENT IN “STUDENT.CSV” FILE.
def modify():
    with open('student.csv','r',newline='\r\n') as f:
        l=[]
        for i in csv.reader(f):
            if int(i[4])<50:
                i[4]=int(i[4])+10
                i[6]=float(i[6])+2
            l.append(i)
    with open('student.csv','w',newline='\r\n') as f:
        csv.writer(f).writerows(l)
    print('Updated Contents of file:')
    display()

## DELETE(): TO DELETE ALL STUDENTS WHOSE AVERAGE IS LESS THAN 40%.THE CHANGE MUST BE EVIDENT IN “STUDENT.CSV” FILE.
def delete():
    with open('student.csv','r',newline='\r\n') as f:
        l=[]
        for i in csv.reader(f):
            if float(i[6])>40:
                l.append(i)
    with open('student.csv','w',newline='\r\n') as f:
        csv.writer(f).writerows(l)
    print('Updated contents of file:')
    display()

opt='y'
while opt in 'yY':
    print('1. Create\n2. Display\n3. Search\n4. Append\n5. Failure\n6. Highest\n7. Modify\n8. Delete')
    ch=int(input("Enter your choice: "))
    if ch==1:
        create()
    if ch==2:
        display()
    if ch==3:
        search()
    if ch==4:
        append()
    if ch==5:
        failure()
    if ch==6:
        highest()
    if ch==7:
        modify()
    if ch==8:
        delete()
    if 0<ch>8:
        print('Please enter a number between 1 and 8')
    opt=input('Would you like to continue: ')

# Menu driven program to create CSV file to store student details (GR No, name, marks, class), insert 5 records (User input), read the records and display all records of the file, display only those records where marks are greater than 80, increase marks by 10 if student got less than 50 and delete the record of the student where GR No is 1234
import csv

def display():
    with open('student.csv','r',newline='\n') as f:
        for i in csv.reader(f):
            print(i)

def create():
    with open('student.csv','w',newline='\n') as f:
        n=int(input('Enter number of students: '))
        for i in range(n):
            grno=int(input('Enter GR No.: '))
            name=input('Enter name: ')
            marks=float(input('Enter marks: '))
            clas=int(input('Enter class: '))
            csv.writer(f).writerow([grno,name,marks,clas])
    display()

def insert():
    with open('student.csv','a',newline='\n') as f:
        for i in range(5):
            grno=int(input('Enter GR No.: '))
            name=input('Enter name: ')
            marks=float(input('Enter marks: '))
            clas=input('Enter class: ')
            csv.writer(f).writerow([grno,name,marks,clas])
    display()

def disp_marks_80():
    with open('student.csv','r',newline='\n') as f:
        d=csv.reader(f)
        for i in d:
            if float(i[2])>80.0:
                print(i)

def inc_marks():
    with open('student.csv','r',newline='\n') as f:
        l=[]
        for i in csv.reader(f):
            if float(i[2])<50.0:
                a=int(float(i[2]))
                a+=10
                i[2]=float(a)
                l.append(i)
            else:
                l.append(i)
    with open('student.csv','w',newline='\n') as f:
        csv.writer(f).writerows(l)
    display()

def delete():
    with open('student.csv','r',newline='\n') as f:
        l=[]
        for i in csv.reader(f):
            if int(i[0])!=1234:
                l.append(i)
    with open('student.csv','w',newline='\n') as f:
        csv.writer(f).writerows(l)
    display()

opt='y'
while opt in 'yY':
    print('1. Create\n2. Insert\n3. Display\n4. Display records where marks > 80\n5. Increase marks if less than 50\n6. Delete records where GR Number is 1234')
    ch=int(input("Enter your choice: "))
    if ch==1:
        create()
    if ch==2:
        insert()
    if ch==3:
        display()
    if ch==4:
        disp_marks_80()
    if ch==5:
        inc_marks()
    if ch==6:
        delete()
    if 0<ch>8:
        print('Please enter a number between 1 and 6')
    opt=input('Would you like to continue: ')