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
