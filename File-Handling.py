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

# Create new file in program and enter three names
namefile=open('names.txt','w')
for i in range(3):
    n=input('Enter name to enter: ')
    namefile.write(n+'\n')
namefile.flush()
namefile.close()
namefile=open('names.txt','r')
print(namefile.read())
