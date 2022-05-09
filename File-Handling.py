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
print('Q1')
print(poem.read(30))
poem.close()

# Read 10 bytes and then read again 5 bytes
poem=open('poem.txt','r')
print('Q2')
print(poem.read(10))
print(poem.read(5))
poem.close()

# Read entire file
poem=open('poem.txt','r')
print('Q3')
print(poem.read())
poem.close()

# Read file's first three lines (line by line)
poem=open('poem.txt','r')
print('Q4')
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
