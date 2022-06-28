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