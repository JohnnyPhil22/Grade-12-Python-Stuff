# Write roll number, name, gender and marks of student in binary file named myb.dat using dump()
from pickle import *
s={}
r=input('Enter student roll number: ')
n=input('Enter student name: ')
g=input('Enter student gender: ')
m=input('Enter student marks: ')
s[(r+' '+n+' '+g+' '+m)]=1
dump(s,open('myb.dat','wb'))
f=open('myb.dat','rb')
content=load(f)
print(content)

# Binary file called emp.dat and write into it the employee details, available as dictionaries.
from pickle import *
emp,ans=[],'y'
while ans=='y':
    no=int(input('Enter employee number: '))
    n=input('Enter employee name: ')
    s=int(input('Enter employee salary: '))
    emp.append([no,n,s])
    ans=input('Add more? ')
dump(emp,open('emp.dat','wb'))
f=open('myb.dat','rb')
content=load(f)
print(content)

# Write roll number, name and mark from user to binary file as long as needed
from pickle import *
s={}
n=int(input('Enter number of entries: '))
for i in range(n):
    r=input('Enter student roll number: ')
    n=input('Enter student name: ')
    g=input('Enter student gender: ')
    m=input('Enter student marks: ')
    s[(r+' '+n+' '+g+' '+m)]=i+1
dump(s,open('myb.dat','wb'))
f=open('myb.dat','rb')
content=load(f)
print(content)

# Create a binary file called myfile.bin with 2 lines and display all chars until before 'o'
import pickle
newstr=''
with open ('myfile.bin','wb') as f:
    data=eval(input('Enter data: '))
    pickle.dump(data,f)
with open ('myfile.bin','rb') as f:
    content=pickle.load(f)
    for i in content:
        if i=='o':
            break
        else:
            for j in i:
                if j=='o':
                    break
                elif j!='o':
                    newstr+=j
print(newstr)

# Accept n employee records and append to binary file tv. Read the records and display on screen.
import pickle
with open ('tv.bin','wb') as f:
    n=int(input('Enter number of employees: '))
    for i in range(n):
        ed=eval(input('Enter employee data: '))
        pickle.dump(ed,f)
with open ('tv.bin','rb') as f:
    print(pickle.load(f))

# Create binary file called student.bin containing roll number, name and marks of students as dictionary. Search for records with roll numbers 12 or 14. If found, display records.
import pickle
n=int(input('Enter number of students: '))
d,l={},[]
with open ('student.bin','wb') as f:
    for i in range(n):
        rn=int(input('Enter roll number: '))
        name=input('Enter name: ')
        l.append(name)
        m=eval(input('Enter marks: '))
        l.append(m)
        d[rn]=l
    pickle.dump(d,f)
with open ('student.bin','rb') as f:
    sd=pickle.load(f)
    for j in sd:
        if j==12 or j==14:
            print(j,sd[j])

# Check file position after read and read last 15 bytes of file
import pickle
with open('poem.txt','r') as f:
    content=f.read()
with open('poem.bin','wb') as fnew:
    pickle.dump(content,fnew)
with open('poem.bin','rb') as fnew:
    print(pickle.load(fnew))
    print(fnew.tell())
    fnew.seek(-15,2)
    print(fnew.tell())

# Write a menu driven program with user defined functions to create a file, search a particular record, delete a particular record, update a particular record and exit
import pickle
def create():
    with open('file.bin','wb') as f:
        data=eval(input('Enter data to add (as a nested list): '))
        pickle.dump(data,f)
    with open('file.bin','rb') as f:
        print('File data:\n',pickle.load(f))
def search():
    en,emplst,f=eval(input('Enter employee number to search for: ')),[],False
    with open('file.bin','rb') as f:
        emplst=pickle.load(f)
        for i in range(len(emplst)):
            if emplst[i][0]==en:
                print('Employee number:',emplst[i][0])
                print('Employee name:',emplst[i][1])
                print('Employee salary:',emplst[i][2])
                f=True
                break
        else:
            print('Employee records not found')
def delete():
    emplst=[]
    with open('file.bin','rb') as f:
        emplst=pickle.load(f)
    f,en,emplst2=False,int(input('Enter employee number to delete: ')),[]
    for i in range(len(emplst)):
        if emplst[i][0]!=en:
            emplst2.append(emplst[i])
    with open('file.bin','wb') as f:
        pickle.dump(emplst2,f)
    with open('file.bin','rb') as f:
        emplst=pickle.load(f)
        print(emplst)
def update():
    en,emplst,f=eval(input('Enter employee number to update: ')),[],False
    with open('file.bin','rb') as f:
        emplst=pickle.load(f)
        for i in range(len(emplst)):
            if emplst[i][0]==en:
                emplst[i][2]=int(input('Enter new employee salary: '))
                f=True
                break
        else:
            print('Employee records not found')
    with open('file.bin','wb') as f:
        pickle.dump(emplst,f)
    with open('file.bin','rb') as f:
        emplst=pickle.load(f)
        print(emplst)
opt='y'
while opt in 'yY':
    print('1. Create file\n2. Search a particlar record\n3. Delete a particular record\n4. Update a particular record')
    ch=int(input('Enter option (1 to 4): '))
    if ch==1:
        create()
    if ch==2:
        create()
        search()
    if ch==3:
        create()
        delete()
    if ch==4:
        create()
        update()
    if 1>ch<4:
        print('Please enter a valid option')
    opt=input('Do you want to continue: ')

# Write a program to enter item number (int), item name (str), quantity (int) and price (float) in a binary file: 
import pickle
with open('file.bin','wb') as f:
    l1,l2=[],[]
    n=int(input('Enter number of items: '))
    for i in range(n):
        itemno=i+1
        itemname=input('Enter item name: ')
        q=int(input('Enter item quantity: '))
        p=float(input('Enter item price: '))
        l2=[itemno,itemname,q,p]
        l1.append(l2)
    print(l1)
    pickle.dump(l1,f)
with open('file.bin','rb') as f:
    itemnumber=int(input('Enter item number to print details for: '))
    content=pickle.load(f)
    for i in range(len(content)):
        if itemnumber==content[i][0]:
            print('Item number:',content[i][0])
            print('Item name:',content[i][1])
            print('Item quantity:',content[i][2])
            print('Item price:',content[i][3])
            print('Item amount:',int(content[i][2])*int(content[i][3]))

# Enter staff details into a file, then search and display content of file where staff code is 13933
import pickle
with open('staff.dat','wb') as f:
    n=int(input('Enter number of records: '))
    d={}
    for i in range(n):
        no=int(input('Enter member number: '))
        na=input('Enter name: ')
        d['Member number']=no
        d['Member name']=na
        pickle.dump(d,f)
    f.seek(0,0)
print('Employee with staff number 13933: ')
with open('staff.dat','rb') as f:
    filedata=pickle.load(f)
    if filedata['Member number']==13933:
        print(filedata)

# Create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message.
import pickle
with open('staff.dat','wb') as f:
    n=int(input('Enter number of records: '))
    mainl=[]
    for i in range(n):
        subl=[]
        no=int(input('Enter roll number: '))
        na=input('Enter name: ')
        subl.append(no)
        subl.append(na)
        mainl.append(subl)
    pickle.dump(mainl,f)
    f.seek(0,0)
rollnotocheck=int(input('Enter roll number to check: '))
with open('staff.dat','rb') as f:
    filedata=pickle.load(f)
    for i in filedata:
        if i[0]==rollnotocheck:
            print(i)
    else:
        print('Roll number doesn\'t exist')

# Create a binary file with roll number, name, and marks. Input a roll number and update the marks.
import pickle
with open('staff.dat','wb') as f:
    n=int(input('Enter number of records: '))
    mainl=[]
    for i in range(n):
        subl=[]
        no=int(input('Enter roll number: '))
        na=input('Enter name: ')
        ma=float(input('Enter mark: '))
        subl.append(no)
        subl.append(na)
        subl.append(ma)
        mainl.append(subl)
    pickle.dump(mainl,f)
    f.seek(0,0)
rollnotomodify=int(input('Enter roll number: '))
with open('staff.dat','rb') as f:
    filedata=pickle.load(f)
    for i in filedata:
        if i[0]==rollnotomodify:
            print(i)
            marktomodify=float(input('Enter new mark: '))
            i[2]=marktomodify
            print(i)
    else:
        print('Roll number doesn\'t exist')

# Menu driven program using functions to perform:
## 1. CREATE(): To create an 'EMP.DAT' file having 'n' records having following details
### a. EID
### b. ENAME 
### c. ESAL 
### d. EDESIG 
### e. DOJ (List containing [Day,Month,Year] of integer data type)
### Write all these details for every record as a dictionary into the file
import pickle
def create():
    with open('emp.dat','ab') as f:
        n=int(input('Enter number of employees: '))
        for i in range(n):
            eid=input('Enter employee ID: ')
            ename=input('Enter employee name: ')
            esal=float(input('Enter employee salary: '))
            edesig=input('Enter employee designation: ')
            doj=eval(input('Enter employee date of joining as list: '))
            pickle.dump({ename:[eid,esal,edesig,doj]},f)

## 2. DISPLAY(): TO DISPLAY THE CONTENTS OF THE FILE WHOSE FILE NAME IS INPUT BY THE USER 
def display():
    with open('emp.dat','rb') as f:
        try:
            while True:
                filedata=pickle.load(f)
                for i in filedata:
                    print(filedata[i])
        except:
            f.close()

## 3. SEARCHNAME(): TO SEARCH AND DISPLAY FOR GIVEN NAME AS INPUT BY THE USER, GIVE APPROPRIATE MESSAGE IF RECORD NOT FOUND.
def searchname():
    flag=0
    nametosearch=input("Enter name: ")
    with open('emp.dat','rb') as f:
        try:
            while True:
                filedata=pickle.load(f)
                for i in filedata:
                    if i==nametosearch:
                        print(filedata[i])
                        flag=1
                        break
        except:
            if flag!=1:
                print('Name not found')
            f.close()

## 4. SEARCHID(): TO SEARCH AND DISPLAY FOR GIVEN ID AS INPUT BY THE USER, GIVE APPROPRIATE MESSAGE IF RECORD NOT FOUND.
def searchid():
    c=3
    q=input("Enter ID: ")
    with open('emp.dat','rb') as f:
        try:
            while True:
                filedata=pickle.load(f)
                a=list(filedata.values())
                for i in filedata:
                    if a[0][0]==q:
                        print(filedata[i])
                        c=4
                        break
        except:
            if c!=4:
                print('EID not found') 
            f.close()

## 5. APPEND() : TO ADD ADDITIONAL ‘N’ RECORDS INTO “EMP.DAT”.
def append():
    with open('emp.dat','ab') as f:
        n=int(input('Enter number of employees: '))
        for i in range(n):
            eid=input('Enter employee ID: ')
            ename=input('Enter employee name: ')
            esal=float(input('Enter employee salary: '))
            edesig=input('Enter employee designation: ')
            doj=eval(input('Enter employee date of joining as list: '))
            pickle.dump({ename:[eid,esal,edesig,doj]},f)

## 6. SEARCHMONTH(): TO COUNT THE TOTAL NO. OF EMPLOYEES AND DISPLAY THEIR DETAILS WHO HAVE JOINED IN A PARTICULAR MONTH (MONTH IS USER INPUT).
def searchmonth():
    count=0
    n=int(input("Enter the month in number: "))
    with open('emp.dat','rb') as f:
        try:
            while True:
                filedata=pickle.load(f)
                count+=1
                for i in filedata:
                    if filedata[i][4][1]==n:
                        print(filedata[i])
                        break
        except:
            print('Total number of employees:',count)
            f.close()

## 7. COPY(): TO COPY THE RECORDS , WHERE DESIG IS MANAGER INTO ANOTHER FILE CALLED “MANAGER.DAT”
def copy():
    c=[]
    with open('emp.dat','rb') as f:
        filedata=pickle.load(f)
        for i in filedata:
            if 'managerMANAGER' in filedata[i][3]:
                c.append(filedata[i])
    with open('manager.dat','ab') as fnew:
        for i in c:
            pickle.dump(c,fnew)

## 8. MODIFYSAL() : TO MODIFY SALARY OF THOSE EMPLOYEES WHERE SALARY IS LESS THAN 3000 ,BY ADDING 500 TO THEIR EXISTING SALARY.
def modifysal():
    c=[]
    with open('emp.dat','rb+') as f:
        try:
            while True:
                filedata=pickle.load(f)
                for i in filedata:
                   if filedata[i][2]<3000:
                       filedata[i][2]+=500
                c.append(filedata)
        except:
            f.seek(0)
            for i in c:
                pickle.dump(i,f)
            f.close()

## 9. DELETEDESIG() : TO DELETE ALL EMPLOYEES WHERE DESIG IS “SALES” 
def deletedesig():
    c=[]
    with open('emp.dat','rb+') as f:
        try:
            while True:
                filedata=pickle.load(f)
                for i in filedata:
                    if 'salesSALES' not in filedata[i][3]:
                        c.append(filedata)
        except:
            f.seek(0)
            for i in c:
                pickle.dump(i,f)
            f.close()

## 10. DELETEID(): TO DELETE EMPLOYEE RECORD WITH THE GIVEN ID, GIVE APPROPRIATE MESSAGE IF RECORD NOT FOUND
def deleteid():
    q=input("Enter employee ID: ")
    a=1
    c=[]
    with open('emp.dat','rb+') as f:
        try:
            while True:
                filedata=pickle.load(f)
                for i in filedata:
                    if filedata[i][0]!=q:
                        c.append(filedata)
                    else:
                        a=2
        except:
            if a==1:
                print('Record not found')
            f=open('emp.dat','wb')
            for i in c:
                pickle.dump(i,f)
            f.close()

opt='y'
while opt in 'yY':
    print('1. Create\n2. Display\n3. Search Name\n4. Search ID\n5. Append\n6. Search Month\n7. Copy\n8. Modify Salary\n9. Delete Designation\n10. Delete ID')
    ch=int(input("Enter option (1 to 10): "))
    if ch==1:
        create()
    if ch==2:
        display()
    if ch==3:
        searchname()
    if ch==4:
        searchid()
    if ch==5:
        append()
    if ch==6:
        searchmonth()
    if ch==7:
        copy()
    if ch==8:
        modifysal()
    if ch==9:
        deletedesig()
    if ch==10:
        deleteid()
    if 0<ch>10:
        print('Please enter a number between 1 and 10.')
    opt=input('Do you wish to continue: ')

# WRITE A MENU DRIVEN PROGRAM IN PYTHON, USING FUNCTIONS TO PERFORM THE FOLLOWING: 
## 1. CREATE() : TO CREATE A “STUDENT.DAT” FILE CONTAINING N RECORDS HAVING THE FOLLOWING DETAILS: 
### a. ROLL 
### b. NAME OF STUDENT 
### c. MARKS 
### d. HOUSE
### WRITE ALL THESE DETAILS FOR EVERY RECORD AS A LIST INTO THE FILE.
import pickle
def create():
    n=int(input("Enter the number of entries: "))
    with open('student.dat','wb') as f:
        for i in range(n):
            rn=int(input("Enter roll number: "))
            na=input("Enter name: ")
            ma=int(input('Enter marks: '))
            ho=input("Enter house: ")
            pickle.dump([rn,na,ma,ho],f)

## 2. DISPLAY(): TO DISPLAY THE CONTENTS OF THE FILE WHOSE FILE NAME IS INPUT BY THE USER 
def display():
    with open('student.dat','rb') as f:
        try:
            while True:
                print(pickle.load(f))
        except:
            f.close()

## 3. SEARCHNAME(): TO SEARCH AND DISPLAY FOR GIVEN NAME AS INPUT BY THE USER , GIVE APPROPRIATE MESSAGE IF RECORD NOT FOUND. 
def searchname():
    flag=0
    name=input("Enter name: ")
    with open('student.dat','rb') as f:
        try:
            while True:
                filedata=pickle.load(f)
                if filedata[1]==name:
                    print(filedata)
                    flag=1
        except:
            if flag!=1:
                print('Name not found')
            f.close()

## 4. SEARCHID(): TO SEARCH AND DISPLAY FOR GIVEN ROLL AS INPUT BY THE USER , GIVE APPROPRIATE MESSAGE IF RECORD NOT FOUND.
def searchid():
    flag=0
    rollnumber=int(input("Enter roll number: "))
    with open('student.dat','rb') as f:
        try:
            while True:
                filedata=pickle.load(f)
                if filedata[0]==rollnumber:
                    print(filedata)
                    flag=1
        except:
            if flag!=1:
                print('Roll number not found')
            f.close()

## 5. APPEND() : TO ADD ADDITIONAL ‘N’ RECORDS INTO “STUDENT.DAT”. 
def append():
    n=int(input("Enter the number of entries: "))
    with open('student.dat','ab') as f:
        for i in range(n):
            rn=int(input("Enter roll number: "))
            na=input("Enter name: ")
            ma=int(input('Enter marks: '))
            ho=input("Enter house: ")
            pickle.dump([rn,na,ma,ho],f)

## 6. COUNT() : TO COUNT THE TOTAL NO.OF RECORDS IN THE FILE.ALSO FIND THE AVERAGE OF ALL THE STUDENTS IN THE FILE
def count():
    count,total=0,0
    with open('student.dat','rb') as f:
        try:
            while True:
                filedata=pickle.load(f)
                count+=1
                total+=filedata[2]
        except:
            print('Total number of students: ',count)
            print('Average marks: ',total/count)
            f.close()

## 7. HIGHEST(): TO COPY THE RECORDS OF STUDENTS WHOSE MARK IS > 90 INTO ANOTHER FILE CALLED “HIGH.DAT”
def highest():
    highmarklist=[]
    with open('student.dat','rb') as f:
        try:
            while True:
                filedata=pickle.load(f)
                if filedata[2]>90:
                    highmarklist.append(filedata)
        except:
            f.close()
    with open('high.dat','ab') as fnew:
        pickle.dump(highmarklist,fnew)

## 8. MODIFY() : TO MODIFY MARKS OF THOSE STUDENTS WHERE MARKS IS LESS THAN 23 ,BY ADDING 10 TO THEIR EXISTING MARK.
def modify():
    modmarklist=[]
    with open('student.dat','rb+') as f:
        try:
            while True:
                filedata=pickle.load(f)
                if filedata[2]<23:
                    filedata[2]+=10
                modmarklist.append(filedata)
        except:
            f.seek(0)
            for i in modmarklist:
                pickle.dump(i,f)
            f.close()

## 9. DELETE() : TO DELETE ALL STUDENTS WHERE HOUSE IS “EMERALD” 
def delete():
    notemelist=[]
    with open('student.dat','rb+') as f:
        try:
            while True:
                filedata=pickle.load(f)
                if 'emeraldEMERALD' not in filedata[3]:
                    notemelist.append(filedata)
        except:
            f.close()
            with open('student.dat','wb') as f:
                for i in notemelist:
                    pickle.dump(i,f)

## 10. DELETEROLL(): TO DELETE STUDENT RECORD WITH THE GIVEN ROLL , GIVE APPROPRIATE MESSAGE IF RECORD NOT FOUND
def deleteroll():
    notgivroll,flag=[],0
    q=int(input("Enter roll: "))
    with open('student.dat','rb+') as f:
        try:
            while True:
                filedata=pickle.load(f)
                if filedata[0]!=q:
                    notgivroll.append(filedata)
                else:
                    flag=1
        except:
            if flag==0:
                print('Not found')
            f.close()
            with open('student.dat','wb') as f:
                for i in notgivroll:
                    pickle.dump(i,f)

opt='y'
while opt in 'yY':
    print('1. Create\n2. Display\n3. Search Name\n4. Search ID\n5. Append\n6. Count\n7. Highest Marks\n8. Modify Marks\n9. Delete House\n10. Delete Roll')
    ch=int(input("Enter your choice: "))
    if ch==1:
        create()
    if ch==2:
        display()
    if ch==3:
        searchname()
    if ch==4:
        searchid()
    if ch==5:
        append()
    if ch==6:
        count()
    if ch==7:
        highest()
    if ch==8:
        modify()
    if ch==9:
        delete()
    if ch==10:
        deleteroll()
    if 0<ch>10:
        print('Please enter a number between 1 and 10.')
    opt=input('Do you wish to continue: ')

# Menu driven program to:
## 1. Create binary file stock.dat to store details of product PCode, PName, Price, Brand
## 2. Insert 5 records
## 3. Read and display all records
## 4. Display total price of all products
## 5. Increase price of products by 10 if brand name is 'Adil'
## 6. Delete record of product if price is greater than 50

import pickle
def create():
    with open ('stock.dat','wb') as f:
        pass

def insert():
    with open ('stock.dat','wb') as f:
        x = int(input('Enter number of Records: '))
        temp = []
        for i in range(x):
            Pcode = int(input('Enter Pcode: '))
            Pname = input('Enter Pname: ')
            Price = int(input('Enter Price: '))
            Brand = input('Enter Brand: ')
            temp.append([Pcode,Pname,Price,Brand])
        pickle.dump(temp,f)

def read():
    with open ('stock.dat','rb') as f:
        x = pickle.load(f)
        print(x)

def total():
    with open ('stock.dat','rb') as f:
        x = pickle.load(f)
        count = 0
        for i in x:
            count += int(i[-2])
    print('Total price is: ',count)

def increase():
    with open ('stock.dat','rb') as f:
        x = pickle.load(f)
        temp = []
        for i in x:
            if i[-1].lower() == 'adil':
                y = i[-2]
                i[-2] = int(y)+10
                temp.append(i)
            else:
                temp.append(i)
    with open ('stock.dat','wb') as f:
        pickle.dump(temp,f)

def delete():
    with open ('stock.dat','rb') as f:
        x = pickle.load(f)
        temp = []
        for i in x:
            if int(i[-2]) > 50:
                pass
            else:
                temp.append(i)
    with open ('stock.dat','wb') as f:
        pickle.dump(temp,f)

condn = True

while condn == True:
    print('Choose\n1.Open File\n2.Insert Records\n3.Read Records\n4.Display Price\n5.Increase\n6.Delete\n7.Exit')
    x = int(input('Enter choice: '))
    if x == 1:
        create()
        print()
    if x == 2:
        insert()
        print()
    if x == 3:
        read()
        print()
    if x == 4:
        total()
        print()
    if x == 5:
        increase()
        print()
    if x == 6:
        delete()
        print()
    if x == 7:
        condn = False