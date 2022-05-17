###########################################
############### TEXT FILES ################
###########################################

earthday=open('blebleble.txt','r')
# Read entire file
print(earthday.read())
earthday.close()
# Read first 22 chars
print(earthday.read(22))
earthday.close()
# Read first two line
print(earthday.readline())
print(earthday.readline())
earthday.close()
# Read first 43 chars
print(earthday.read(43))
earthday.close()
# Read first 5 chars for each loop
s=' '
while s:
    s=earthday.readline(5)
    print(s,end='\n')
earthday.close()
# Print each line in file
for s in earthday:
    print(s,end='\n')
earthday.close()

# Read a file's first 30 bytes and print it
poem=open('poem.txt','r')
print(poem.read(30))
poem.close()

# Read 10 bytes and then read again 5 bytes
poem=open('poem.txt','r')
print(poem.read(10))
print(poem.read(5))
poem.close()

# Read n bytes and then read again x bytes till end of file
poem=open('poem.txt','r')
n=int(input('Enter number of bytes to read: '))
print(poem.read(n))
print(poem.read())
poem.close()

# Read entire file
poem=open('poem.txt','r')
print(poem.read())
poem.close()

# Read file's first three lines (line by line)
poem=open('poem.txt','r')
for i in range(3):
    print(poem.readline())
poem.close()

# Display each word of a line separately
poem=open('poem.txt','r')
content=poem.readlines()
for l in content:
    word=l.split()
    print(word)
poem.close()

# Give each line of a file
poem=open('poem.txt','r')
content=poem.readlines()
for l in content:
    word=l.splitlines()
    print(word)
poem.close()

# Calculate size of file with and without EOL and blank lines.
poem=open('poem.txt','r')
data=poem.readlines()
content=''
for i in data:
    content+=i
print('File size:',len(content),'characters')
poem=open('poem.txt','r')
data=poem.readlines()
content=''
for i in data :
    for j in i :
        if j.isalnum():
            content+=j
print('File size without EOL and blank lines:',len(content),'characters')
poem.close()

# Read complete file in list
poem=open('poem.txt','r')
print(poem.readlines())
poem.close()

# Calculate size of file in bytes and number of lines.
poem=open('poem.txt','r')
data=poem.readlines()
content=''
for i in data:
    content+=i
print('File size:',len(content)/8,'bytes')
poem=open('poem.txt','r')
data=poem.readlines()
content=''
for i in data :
    for j in i :
        if j.isalnum():
            content+=j
print('File size without EOL and blank lines:',len(content)/8,'bytes')
poem.close()
poem=open('poem.txt','r')
data=poem.readlines()
count=0
for i in data:
    word=i.splitlines()
    count+=1
print('File size:',count,'lines')

# Create new file in program and enter 'n' names
namefile=open('names.txt','w')
lon=eval(input('Enter list of names: '))
namefile.writelines(lon)
namefile.close()
namefile=open('names.txt','r')
print(namefile.read())

# Count how many times 'a' is present in file
f=open('blebleble.txt','r')
data=f.readlines()
count=0
for i in data:
    for j in i:
        if j=='a':
            count+=1
print('Frequency of \'a\' in file:',count)

# Replace 'E' with 'I' while displaying content of file
f=open('blebleble.txt','r')
s=f.read().replace('E','I')
f.close()
f=open('blebleble.txt','w')
f.write(s)
f.flush()
f=open('blebleble.txt','r')
print(f.read())

# Display how many uppercase chars and digits are present
f=open('blebleble.txt','r')
data=f.readlines()
countc,countd=0,0
for i in data:
    for j in i:
        if j.isupper():
            countc+=1
        if j.isdigit():
            countd+=1
print('Number of uppercase characters:',countc,'\nNumber of digits:',countd)

# Display how many vowels are present
def isvowel(j):
    return j.upper() in ['A','E','I','O','U']
f=open('blebleble.txt','r')
data=f.readlines()
count=0
for i in data:
    for j in i:
        if isvowel(j):
            count+=1
print('Number of vowels:',count)

# Open file to write new content
f=open('news.txt','w')
f.write('Hello\nThis is a new file\n')
f.close()
# Open file to read existing content
f=open('news.txt','r')
print(f.read())
f.close()
# Open file to add new content to existing content
f=open('news.txt','a')
f.write('News\nMore news\n')
f.close()

# Read content of file and display occurrence of IS, TO and UP
def istoupcount():
    f=open('writer.txt','w')
    f.write('IT IS UP TO US TO TAKE CARE OF OUR SURROUNDING. IT IS NOT POSSIBLE ONLY FOR THE GOVERNMENT TO TAKE RESPONSIBILITY.')
    f.close()
    f=open('writer.txt','r')
    count=0
    word=f.read().split()
    for i in word:
        if i=='IS' or i=='TO' or i=='UP':
            count+=1
    return count
print('Count of IS, UP and TO:',istoupcount())

# Read lines of file and display those lines starting with A or E
def countae():
    with open('writer.txt','w') as f:
        f.write('A clean environment is necessary for our good health.\nWe should clean our environment.\nEducational Institutes should take the lead.')
    f=open('writer.txt','r')
    data=f.readlines()
    for l in data:
        if l[0]=='A' or l[0]=='E':
            print(l)
countae()

# Print file containing serial number, name, author and price of book
f=open('file.txt','w')
l=[]
n=int(input('Enter number of books: '))
for i in range(n):
    name=input('Enter book name: ')
    a=input('Enter author name: ')
    p=input('Enter book price: ')
    l.append(str(i+1)+': '+name+' - '+a+' - '+p+'\n')
f.writelines(l)
f.close()
f=open('file.txt','r')
print(f.read())

# Add roll number, name and marks to dictionary
f=open('file.txt','w')
d={}
n=int(input('Enter number of students: '))
for i in range(n):
    r=input('Enter roll number: ')
    name=input('Enter name: ')
    m=input('Enter marks: ')
    d[str(r+': '+name+' - '+m+'\n')]=i
f.writelines(d)
f.close()
f=open('file.txt','r')
print(f.read())

# Read only 10 chars
f=open('file.txt','r')
print(f.read(10))
f.close()
# Read one line
f=open('file.txt','r')
print(f.readline())
f.close()
# Read complete file
f=open('file.txt','r')
print(f.read())
f.close()

###########################################
############## BINARY FILES ###############
###########################################

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