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
