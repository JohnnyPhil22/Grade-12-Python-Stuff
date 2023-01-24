# Input two numbers and write function which finds the sum of numbers and returns sum
def sum_of_nums(a,b):
    return a+b
x=int(input('Enter number 1: '))
y=int(input('Enter number 2: '))
print('Sum:',sum_of_nums(x,y))

# Input required values and write function to calculate simple interest and return interest
def SI(p,r,t):
    return((p*r*t)/100)
p=eval(input('Enter principal: '))
r=eval(input('Enter rate of interest: '))
t=eval(input('Enter time: '))
print('Simple Interest:',SI(p,r,t))

# Input number and write function to find factorial of number
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print("Factorial of number:",fact)
n=int(input('Enter number: '))
fact(n)

# Input two numbers and write function which returns the bigger number
def findbig(x,y):
    if x>y:
        print(x,'is greater than',y)
    if y>x:
        print(y,'is greater than',x)
x=eval(input('Enter number 1: '))
y=eval(input('Enter number 2: '))
findbig(x,y)

# Calculate simple interest by taking principal, time and rate. Default for rate and time = 10% and 2 years.
def interest(p,r=10,t=2):
    return((p*r*t)/100)
p=eval(input('Enter principal: '))
print('Simple Interest:',interest(p))

# Accept a number and check if prime number
def find(n):
    for i in range(2,n//2+1):
        if n%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")
n=int(input('Enter number: '))
find(n)

# Check if passed string is palindrome
def palindrome(s):
    if s==s[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")
s=input('Enter string: ')
palindrome(s)

# Take binary number and convert to decimal
def btod(b):
	d,i=0,0
	while b!=0:
		dec=b%10
		d=d+dec*pow(2,i)
		b//=10
		i+=1
	print(d)
b=int(input('Enter binary number: '))
btod(b)

# Calculate SI. Default values for rate and time = 10% and 2 years respectively.
def interest(p,t=2,r=10):
    return ((p*r*t)/100)
p=eval(input('Enter principal: '))
ch=input('Do you want to enter rate and time (y/N): ')
if ch=='y' or ch=='Y':
    r=eval(input('Enter rate: '))
    t=eval(input('Enter time: '))
    print('Simple Interest:',interest(p,r,t))
else:
    print('Simple Interest:',interest(p))

# Assess two values and return sum, difference, product and quotient.
def calculator(a,b):
    return (a+b),(a-b),(a*b),(a/b)
a=eval(input('Enter number 1: '))
b=eval(input('Enter number 2: '))
s,d,p,q=calculator(a,b)
print('Sum:',s,'\nDifference:',d,'\nProduct:',p,'\nQuotient:',q)

def multiple(n):
    return n,(n*2),(n*3),(n*4),(n*5)
n=eval(input('Enter number: '))
print(multiple(n))

# Accept variable length argument and count number of odd and even numbers and returns both values
## Method 1
def count(*n):
    ecount,ocount=0,0
    for i in n:
        if i%2==0:
            ecount+=1
        if i%2!=0:
            ocount+=1
    return ecount,ocount
print('Number of even and odd numbers:',count(12,15,664,44,6,64,64,6,8,5,45,4657,6541,651))
## Method 2
def count(l):
	ocount,ecount=0,0
	for i in l:
		if i%2:
			ocount+=1
		else:
			ecount+=1
	return(ocount,ecount)
l=[]
n=int(input('Enter number of elements for list: '))
for i in range(n):
	l.append(int(input('Enter element: ')))
print(l)
print(count(l))

# Take one positive integer and tell if it is odd or even
def chkodd(n):
    if n<=0:
        print('Enter positive value')
    else:
        if n%2==0:
            print('Even number')
        else:
            print('Odd number')
n=int(input('Enter number: '))
chkodd(n)

# Input list and reverse
def rev(l):
    return l[::-1]
l=eval(input('Enter list: '))
print('Reversed list:',rev(l))

# Input two lists and put both together into new list
def append(l1,l2):
    l3=l1+l2
    return l3
l1=eval(input('Enter list 1: '))
l2=eval(input('Enter list 2: '))
print('Combined list:',append(l1,l2))

# Dictionary with key as name and value as mark. Increase mark by 5 if mark is between 90 to 95.
def change(d):
    for j in d:
        if 90<d[j]<95:
            d[j]+=5
    return d
d=eval(input('Enter dictionary: '))
print(change(d))

# Binary Search
def search2(l,low,high,x):
    if high>=low:
        mid=(high+low)//2
        if l[mid]==x:
            return mid
        elif l[mid] > x:
            return search2(l,low,mid-1,x)
        else:
            return search2(l,mid+1,high,x)
    else:
        return -1
l=eval(input('Enter list: '))
x=eval(input('Enter number: '))
result=search2(l,0,len(l)-1,x)
if result!=-1:
    print(x,"is at index",str(result))
else:
    print(x,"not in list")

# Swap two consecutive elements in list
def swap2(l):
    for i in range(len(l)):
        if i%2==0:
            l[i],l[i+1]=l[i+1],l[i]
    return l
l=eval(input('Enter list: '))
print('New list:',swap2(l))

# Merge two lists (first in ascending order and second in descending order)
a=eval(input('Enter list 1: '))
if sorted(a)!=a:
    print('Enter list in ascending order')
else:
    b=eval(input('Enter list 2: '))
    if sorted(b,reverse=True)!=b:
        print('Enter list in descending order')   
    else:
        c=a+b
        print('Merged list in descending order:',sorted(c,reverse=True))

# Bubble Sort
def sortingbubble(l):
    for i in range(len(l)):
        for j in range(0,len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
l=eval(input('Enter list: '))
print('Sorted list:',sortingbubble(l))

# Selection Sort
def sortingselect(l,s):
    for step in range(s):
        min=step
        for i in range(step+1,s):
            if l[i]<l[min]:
                min=i
        l[step],l[min]=l[min],l[step]
    return l
l=eval(input('Enter elements: '))
print('Sorted list:',sortingselect(l,len(l)))

# Insertion Sort
def sortinginsertion(l):
    for i in range(1,len(l)):
        j=i
        while l[j-1]>l[j] and j>0:
            l[j-1],l[j]=l[j],l[j-1]
            j-=1
    return l
l=eval(input('Enter list: '))
print('Sorted list:',sortinginsertion(l))

# Move elements divisible by 5 to end of list
def move(l):
    for i in l:
        if i%5==0:
            l.append(l.pop(l.index(i)))
    return l
l=eval(input('Enter list: '))
print('New list:',move(l))

# Add all odd and even values in a list separately
def AddOddEven(VALUES):
    odd_sum,even_sum=0,0
    for i in VALUES:
        if i%2==0:
            even_sum+=i
        if i%2!=0:
            odd_sum+=i
    print(f'Even sum: {even_sum}')
    print(f'Odd sum: {odd_sum}')
l=eval(input('Enter list of integers: '))
AddOddEven(l)

# Display number of times ID is in list of IDs
def HowMany(ID,Val):
    count=0
    for i in ID:
        if i==Val:
            count+=1
    print(f'{Val} found {count} times')
id_list=eval(input('Enter IDs in list: '))
val=int(input('Enter ID to count: '))
HowMany(id_list,val)

# Swap the first half of list (even number of elements only) with second half of list
def Swapper(Numbers):
    mid=len(Numbers)//2
    for i in range(mid):
        Numbers[i],Numbers[mid+i]=Numbers[mid+i],Numbers[i]
    print(Numbers)
l=eval(input('Enter list of integers (List should have even number of elements): '))
Swapper(l)

# Print count of numbers between 1 and upper limit divisible by 3 or 7
def Count3and7(N):
    count=0
    for i in range(1,N+1):
        if i%3==0 or i%7==0:
            count+=1
    return count
print(Count3and7(int(input('Enter upper limit: '))))

# Method to count occurrence of IS, TO or UP together in file
def ISTOUPCOUNT():
    count=0
    with open('WRITER.TXT') as f:
        for w in f.read().split(' '):
            if w=='IS' or w=='TO' or w=='UP':
                count+=1
    return count
print(ISTOUPCOUNT())