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

# Create a text file and find most commonly occurring word(s)
with open ('file.txt','w+') as a:
    n=eval(input("Enter the string here: "))
    a.write(n)
with open ('file.txt','r') as a:
    c=a.read().split(' ')
b,h='',0
for i in c:
    if i!=' ' and n.count(i)>h:
        b=i
        h=n.count(i)
print('Most common element:',b)

# Write a menu driven program to perform / manipulate a text file called as 'POETIC.TXT' containing n no. of lines. Use the following functions: (Create text file using the create function also after each function execute, call display function to display the contents of the file.)
## CREATE()
def create():
    with open ('poetic.txt','w') as f:
        data=eval(input('Enter data: '))
        f.write(data)

## DISPLAY(): To display the complete contents of the file given by the user.
def display():
    f=open('poetic.txt','r')
    print(f.read())

## COUNTCHAR(): Read the text file and display the number of vowels / consonants / uppercase / lowercase characters in the file.
def countchar():
    f=open('poetic.txt','r')
    content,countv,countc,countu,countl=f.read(),0,0,0,0
    for i in content:
        for j in i:
            if j in 'AEIOUaeiou':
                countv+=1
            if j in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
                countc+=1
            if j.isupper():
                countu+=1
            if j.islower():
                countl+=1
    print('Number of vowels:',countv,'\nNumber of consonants:',countc,'\nNumber of uppercase letters:',countu,'\nNumber of lowercase letters:',countl)

## HASHSHOW(): Read the text file “POETIC.TXT” line by line and display each word separated by a #. 
def hashshow():
    f=open('poetic.txt','r')
    for l in f:
        w=l.split()
        for i in w:
            print(i,end='#')
    print('\n')

## COPY(): Copy all those lines which contains '#' to another file called “special.txt”
def copy():
    f=open('poetic.txt','r')
    fnew=open('special.txt','w')
    newstr=''
    for i in f:
        for j in i:
            if j=='#':
                newstr+=i
    with open ('special.txt','w') as fnew:
        fnew.write(newstr)
    with open ('special.txt','r') as fnew:
        content=fnew.read()
    print('Contents in new file:\n',content)

## REPLACE(): Replace a word with another user given word into another file called 'duplicate.txt' and display both files. 
def replace():
    with open('poetic.txt','r') as f:
        content=f.read()
        print('Contents of poetic.txt:',content)
        w=input('Enter word to be replaced: ')
        nw=input('Enter word to replace old word: ')
    with open('duplicate.txt','w') as fnew:
        newcontent=content.replace(w,nw)
        fnew.write(newcontent)
    with open('duplicate.txt','r') as fnew:
        print('Contents of duplicate.txt:\n',fnew.read())

## DELETE(): Deletes a given word in text file
def delete():
    with open('poetic.txt','r') as f:
        content=f.read()
    with open('poetic.txt','w') as f:
        w=input('Enter word to remove: ')
        content=content.replace(w,'')
        f.write(content)
    with open('poetic.txt','r') as f:
        print(f.read())

## COUNTEND(): Count the no. of lines ending with the character 'y' or 'i' (Do not take into consideration the case of the character) 
def countend():
    count=0
    with open('poetic.txt','r') as f:
        for i in f.readlines():
            if i[-1]=='y' or i[-1]=='Y' or i[-1]=='i' or i[-1]=='I':
                count+=1
    print(count)

## VOWEL(): Copies all words that starts with a vowel to another file called vowel.txt, display both the file content.
def vowel():
    with open(r'poetic.txt','r') as f:
        print('Content in poetic.txt:\n',f.read())
        data=f.readlines()
        for i in data:
            temp=i.split(' ')
            for j in temp:
                if j[0] in 'aeiouAEIOU':
                    with open(r'vowel.txt','a') as fnew:
                        fnew.write(j)
                        fnew.write('\n')
    with open('vowel.txt','r') as fnew:
        print('Content in vowel.txt:\n',fnew.read())

## CHANGE(): Replaces every space with “**” and display both files.
def change():
    with open('poetic.txt','r') as f:
        content=f.read()
    with open('poetic.txt','w') as f:
        content=content.replace(' ','**')
        f.write(content)
    with open('poetic.txt','r') as f:
        print(f.read())

opt='y'
while opt in 'yY':
    print('1. Create file\n2. Display file\n3. Count characters\n4. Show each word separated by a hash\n5. Copy all lines containing a hash to another file\n6. Replace a word with another word into another file\n7. Delete a word\n8. Count the no. of lines ending with y or i\n9. Copies all words that starts with a vowel to another file\n10. Replaces every space with \'**\'')
    ch=int(input('Enter option (1 to 10): '))
    if ch==1:
        create()
        display()
    if ch==2:
        create()
        display()
    if ch==3:
        create()
        countchar()
    if ch==4:
        create()
        hashshow()
    if ch==5:
        create()
        copy()
    if ch==6:
        create()
        replace()
    if ch==7:
        create()
        delete()
    if ch==8:
        create()
        countend()
    if ch==9:
        create()
        vowel()
    if ch==10:
        create()
        change()
    if 1>ch<10:
        print('Please enter a valid option')
    opt=input('Do you want to continue: ')

# Read a text file line by line and display each word separated by a #.
f=open('poetic.txt','r')
for l in f:
    w=l.split()
    for i in w:
        print(i,end='#')

# Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file.
f=open('poetic.txt','r')
content,countv,countc,countu,countl=f.read(),0,0,0,0
print(content)
for i in content:
    for j in i:
        if j in 'AEIOUaeiou':
            countv+=1
        if j in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            countc+=1
        if j.isupper():
            countu+=1
        if j.islower():
            countl+=1
print('Number of vowels:',countv,'\nNumber of consonants:',countc,'\nNumber of uppercase letters:',countu,'\nNumber of lowercase letters:',countl)

# Remove all the lines that contain the character 'a' in a file and write it to another file.
f,fnew=open('poetic.txt','r'),open('newfile.txt','w')
content=f.readlines()
print('Original contents:\n',content)
for i in content:
    if 'a' in i:
        fnew.write(i)
        content.remove(i)
fnew=open('newfile.txt','r')
print('Content of file with lines containing \'a\':\n',fnew.read())

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