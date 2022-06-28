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
        return "underflow"
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
        print("sorry no itmes are in the stack")
    else:
        t=len(s)-1
        print("(Top)",end=' ')
        while(t>=0):
            print(s[t],"<==",end=' ')
            t-=1
        print()
# main program
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
# Create an empty stack - initialize size of stack as 0
def createStack():
	stack=[]
	return stack

# Determine the size of the stack
def size(stack):
	return len(stack)

# Stack is empty if the size is 0
def isEmpty(stack):
	if size(stack) == 0:
		return True

# Function to add an item to stack (increase size by 1)
def push(stack,item):
	stack.append(item)

# Function to remove an item from stack (decreases size by 1)
def pop(stack):
	if isEmpty(stack): return
	return stack.pop()

# A stack based function to reverse a string
def reverse(string):
	n = len(string)
	# Create a empty stack
	stack = createStack()
	# Push all characters of string to stack
	for i in range(0,n,1):
		push(stack,string[i])
	# Making the string empty since all characters are saved in stack
	string=""
	# Pop all characters of string and put them back to string
	for i in range(0,n,1):
		string+=pop(stack)
	return string
	
# Driver program to test above functions
string=input("enter the string:")
string = reverse(string)
print("Reversed string is " + string)

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

# Write a program to implement a stack for these book details (bookno, bookname), i.e., new each item node of the stack contains two types of information – a bookno and its name. Just implement Push and display operations.
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