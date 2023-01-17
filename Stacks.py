# Check if list is empty
def isEmpty(l):
    if len(l)==0:
        return True
    else:
        return False

# Implement stack with menu driven programs to push 10 items in it and pop only even numbers. Display popped items then display stack
def isEmpty(l):
    if len(l)==0:
        return True
    else:
        return False
def push(l,item):
    l.append(item)
    top=len(l)-1
def pop(l):
    if isEmpty(l):
        print('Stack Underflow')
    else:
        for i in l:
            if i%2==0:
                print(i)
    print(l)
l=[]
opt='y'
while opt in 'yY':
    print('1. Add elements\n2. Pop even numbers')
    ch=int(input('Enter choice: '))
    if ch==1:
        for i in range(10):
            item=int(input('Enter number: '))
            push(l,item)
    elif ch==2:
        pop(l)
    else:
        print('Please enter either 1 or 2')
    opt=input('Press y to continue: ')

# Stack Implementation
def isEmpty(s):
    if len(s)==0:
        return True
    else:
        return False
def push(s,item):
    s.append(item)
    top=len(s)-1
def pop(s):
    if isEmpty(s):
        print("Stack Underflow")
    else:
        val=s.pop()
        if len(s)==0:
            top=None
        else:
            top=len(s)-1
        return val
def peek(s):
    if isEmpty(s):
        return "Underflow"
    else:
        top=len(s)-1
        return s[top]
def display(s):
    if isEmpty(s):
        print("Empty stack")
    else:
        t=len(s)-1
        print("(Top)",end=' ')
        while(t>=0):
            print(s[t],"<==",end=' ')
            t-=1
        print()
s=[]
top=None
print("stack implemetation")
print("1. PUSH")
print("2. POP")
print("3. PEEK")
print("4. DISPLAY STACK")
print("0. EXIT")
while True:
      ch=int(input("ENTER YOUR CHOICE(1,2,3,4,0):"))
      if ch==1:
           val=int(input("enter the value to push:"))
           if val%2==0:
              push(s,val)
              print("it is divisible by 2")
           else:
               print("number is not divisible")
               
      elif ch==2:
            val=pop(s)
            if val=="underflow":
                  print("empty stack")
            else:
                 print("deleted item is:",val)
      elif ch==3:
            val=peek(s)
            if val=="underflow":
                  print("empty stack")
            else:
               print("Top item is:",val)
      elif ch==4:
           display(s)
      elif ch==0:
           print("bye")
           break

# Reverse String
def createStack():
    stack=[]
    return stack
def size(stack):
    return len(stack)
def isEmpty(stack):
    if size(stack)==0:
        return True
def push(stack,item):
    stack.append(item)
def pop(stack):
    if isEmpty(stack): return
    return stack.pop()
def reverse(string):
    n=len(string)
    stack=createStack()
    for i in range(n):
        push(stack,string[i])
    string=""
    for i in range(n):
        string+=pop(stack)
    return string
print("Reversed string: "+reverse(input("Enter string: ")))

# Create stack with odd numbers out of all numbers entered. Display stack content with largest number.
def create_stack_and_display():
    l,onl=eval(input('Enter list: ')),[]
    for i in l:
        if i%2!=0:
            onl.append(i)
    if len(l)==0:
        print('Empty Stack')
    else:
        print('Original stack:',l,'\nLargest number in original stack:',max(l),'\nOdd number stack:',onl,'\nLargest number in odd number stack:',max(onl))
create_stack_and_display()

# Print numbers divisible by 3 or 5 from list
def push3_5(n):
    only3_5=[]
    for i in n:
        if i%3==0 or i%5==0:
            only3_5.append(i)
    print(only3_5)
    return only3_5
num=[]
for i in range(5):
    n=int(input("Enter number: "))
    num.append(n)
print(num)
only3_5=push3_5(num)
for i in range(len(only3_5)):
    print('[',only3_5.pop(),']')
print("Stack empty")

# Function insert(Arr) where Arr is a list of numbers. From this list push all numbers divisible by 5 into a stack implemented by using a list. Display stack if it has at least one element otherwise display appropriate error message.
def insert(Arr):
    l=[]
    for i in Arr:
        if i%5==0:
            l.append(i)
    if len(l)>=1:
        for j in l:
            print('[',j,']')
    else:
        print('Stack empty')
insert(eval(input('Enter list: ')))

# Functions PushS(list) and PopS(List) for performing push and pop operations with a stack of list containing integers
def pushs(l):
    n=int(input('Enter number of numbers to add: '))
    for i in range(n):
        number=int(input('Enter number to add: '))
        l.append(number)
    print(l)
def pops(l):
    for i in range(len(l)):
        print(l.pop())
    print('Stack Empty')
l=eval(input('Enter list: '))
pushs(l)
pops(l)

# Functions MakePush(Package) and MakePop(Package) to add and delete a Package from a list of Package Descriptions (basically push and pop operations in a stack)
def MakePush(Package):
    n=int(input('Enter number of packages to add: '))
    for i in range(n):
        package=input('Enter package to add: ')
        Package.append(package)
    print(Package)
def MakePop(Package):
    for i in range(len(Package)):
        print(Package.pop())
    print('Stack Empty')
l=eval(input('Enter list: '))
MakePush(l)
MakePop(l)

# Implement a stack for these book details (bookno, bookname), i.e., new each item node of the stack contains two types of information – a bookno and its name. Just implement Push and display operations.
top=None
def pop(d):
    for a in range(len(d)-1,-1,-1):
        print(d.pop())
        if len(d)==0:
            print('Stack empty')
def books():
    n=int(input('Enter number of books: '))
    l=[]
    for i in range(n):
        info=eval(input('Enter book '+str(i+1)+' info: '))
        l.append(info)
    print(l)
    print(pop(l))
print(books())

# A grocery shop implements its inventory as a stack and each item is entered with the following details: Item Number, Name, Quantity, Price. Write a program which uses function Push and Pop that adds and removes an item from the stack.
l=[]
def push():
    global l
    n=int(input('Enter number of items: '))
    for i in range(n):
        d={}
        item=int(input('Enter item code: '))
        name=input('Enter item name: ')
        quan=int(input('Enter item quantity: '))
        pric=float(input('Enter item price: '))
        temp=[name,quan,pric]
        d[item]=temp
        l.append(d)
    print(l)
def pop(l):
    for i in range(len(l)):
        det=l[i]
        for key in det:
            y=det[key]
            if y[1]<10:
                print(det)
push()
pop(l)

# Implement stack to input, push and display student IDs and their names.
def push(d):
    l=[]
    for i in d:
        if d[i][0].lower()=='a':
            l.append(i)
    return l
def display (l,d):
    for i in range(-1,-len(l)-1,-1):
        print(d.get(l[i]),end=' ')
    print('Empty Stack')
ch=input('Enter y to continue: ')
while ch in 'Yy':
    print('1. Input Dictionary\n2. Push\n3. Display\n4. Exit')
    opt=int(input('Enter choice: '))
    if opt==1:
        d={}
        n=int(input('Enter number of students: '))
        for j in range(n):
            id=input('Enter ID number: ')
            name=input('Enter name: ')
            d[id]=name
    elif opt==2:
        m=push(d)
        print(m)
    elif opt==3:
        m=push(d)
        display(m,d)
    elif opt==4:
        ch='v'
    else:
        print('Enter valid number')

# Write a program to implement a list of numbers as stack with push, pop, peek and display options.
def push(l):
    numtoadd=eval(input("Enter number: "))
    l.append(numtoadd)
    print('New stack:',l)

def peek(l):
    print(l[-1])

def display(l):
    print(l)

def pop(l):
    for i in range(len(l)):
        if len(l)==0:
            print('Empty stack')
            break
        else:
            print(l.pop())
    print('Empty stack')

l=eval(input("Enter the list: "))
opt='y'
while opt in 'yY':
    print('1. Push\n2. Peek\n3. Display\n4. Pop')
    ch=int(input("Enter your choice: "))
    if ch==1:
        push(l)
    if ch==2:
        peek(l)
    if ch==3:
        display(l)
    if ch==4:
        pop(l)
    if 0<ch>4:
        print('Please enter a number between 1 and 4')
    opt=input('Do you wish to continue: ')

# Write a program to implement a stack named as train, containing [train no, train name]. Using functions implement all permissible operations on a stack.
def push(l):
    number=int(input("Enter train number: "))
    name=input("Enter train name: ")
    l.append([number,name])
    print('New stack:',l)

def peek(l):
    print(l[-1])

def display(l):
    print(l)

def pop(l):
    for i in range(len(l)):
        if len(l)==0:
            print('Empty stack')
            break
        else:
            print(l.pop())
    print('Empty stack')

train=[]
n=int(input("Enter number of entries: "))
for i in range(n):
    number=int(input("Enter train number: "))
    name=input("Enter train name: ")
    train.append([number,name])
opt='y'
while opt in 'yY':
    print('1. Push\n2. Peek\n3. Display\n4. Pop')
    ch=int(input("Enter your choice: "))
    if ch==1:
        push(train)
    if ch==2:
        peek(train)
    if ch==3:
        display(train)
    if ch==4:
        pop(train)
    if 0<ch>4:
        print('Enter a number between 1 and 4')
    opt=input('Do you wish to continue: ')

# Write a program to create a stack contaning student names, and manipulate the stack by peforming the following instructions.
# Insert()
def insert(s):
    name=input("Enter name: ")
    s.append(name)
    print(s)

# Delete()
def delete(s):
    s.pop(0)
    print(s)

# Peek()
def peek(s):
    print(s[0])

# Display()
def display(s):
    print(s)

l=[]
n=int(input("Enter number of entries: "))
for i in range(n):
    name=input("Enter name: ")
    l.append(name)

opt='y'
while opt in 'yY':
    print('1. Insert\n2. Display\n3. Peek\n4. Delete')
    ch=int(input("Enter your choice: "))
    if ch==1:
        insert(l)
    if ch==2:
        display(l)
    if ch==3:
        peek(l)
    if ch==4:
        delete(l)
    if 0<ch>4:
        print('Please enter a number between 1 and 4')
    opt=input('Do you wish to continue: ')

# Write a function in python, insert(Arr), where Arr is a list of numbers. From this list push all the numbers divisible by 5 into a stack implemented by using a list . Display the stack if it has at least one element, otherwise display appropriate error message.
numdiv5=[]
Arr=eval(input('Enter list of numbers: '))
def insert(Arr,s):
    for i in Arr:
        if i%5==0:
            s.append(i)
insert(Arr,numdiv5)
if len(numdiv5)>0:
    print('Stack of numbers divisible by 5:',numdiv5)
else:
    print('Empty stack')

# Write addnew(book), remove(book) methodsin python to add a new book and remove a book from a list of books, considering them to act as Push and Pop operations of the data structure stack.
book=eval(input("Enter list of book names: "))

def addnew(book):
    booknametoadd=input("Enter book name: ")
    book.append(booknametoadd)
    print(book)

def remove(book):
    if len(book)!=0:
        print(book.pop())
    else:
        print('Empty stack')

opt='y'
while opt in 'yY':
    print('1. Add\n2. Remove')
    ch=int(input("Enter your choice: "))
    if ch==1:
        addnew(book)
    if ch==2:
        remove(book)
    if 1<ch>2:
        print('Please enter either 1 or 2')
    opt=input('Do you wish to continue: ')

# Write a function in python POP(Arr), where Arr is a stack implemented by list of number. The function returns the value deleted from the stack.
def POP(Arr):
    print(Arr.pop())
Arr=eval(input("Enter list: "))
POP(Arr)

# Push uppercase alphabets of string into stack and pop & display contents of stack
def pop(l):
    for i in range(len(l)):
        print(l.pop(),end=' ')
def push(s):
    l=[]
    for i in s:
        if i.isupper():
            l.append(i)
    pop(l)
s=input('Enter string: ')
push(s)

# Push positive numbers from list of numbers into stack and pop & display contents of stack
def pop(l):
    for i in range(len(l)):
        print(l.pop(),end=' ')
def push(s):
    l=[]
    for i in s:
        if int(i)>0:
            l.append(i)
    pop(l)
s=eval(input('Enter list: '))
push(s)

# A grocery shop implements its inventory as a stack I and each item is a dictionary with key as Icode and value a list with Iname and price. Write user defined functions to push to a stack I an item detail inputted by the user, pop an item from stack I and display the popped item, display the stack and exit
def push():
    global l
    l=[]
    n=int(input('Enter number of items: '))
    for i in range(n):
        d={}
        icode=int(input('Enter item code: '))
        iname=input('Enter item name: ')
        price=float(input('Enter item price: '))
        d[icode]=[iname,price]
        l.append(d)

def pop():
    print('Popped element:\n')
    print(l.pop())

def display():
    print('Stack:\n')
    for i in range(len(l)-1,-1,-1):
        print(l[i])

opt='y'
while opt in 'yY':
    print('1. Push to stack\n2. Pop an element\n3. Display\n4. Exit')
    ch=int(input('Enter choice: '))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        opt='N'
    opt=input('Do you wish to continue: ')