#types of arguments
#positional args
def form(name,mail,ph,age):
    print('Name is:' , name)
    print('mail is:' , mail)
    print('ph is:' , ph)
    print('age is:' , age)
form('Harshita','yadavharshita2401@gmail.com',8306438617,21)
#default and keyword
def form(name,mail,ph,age=21,alt_phn=None):
    print('Name is:' , name)
    print('mail is:' , mail)
    print('ph is:' , ph)
    print('age is:' , age)
form('Harshita','yadavharshita2401@gmail.com',8306438617,alt_phn=8934287682)

def form(**a):
    print('a',a)
    print(len(a))
    # print('Name is:' , name)
    # print('mail is:' , mail)
    # print('ph is:' , ph)
    # print('age is:' , age)
form(a='Harshita',b='yadavharshita2401@gmail.com',c=8306437)

#task
def form(name,age,city,clg,state='Rajasthan'):
    print('Name: ',name)
    print('age: ',age)
    print('city: ',city)
    print('state: ',state)
    print('clg: ',clg)
  
form(input('Enter name: '),input('Enter age: '),input('Enter city: '),clg='jecrc')

#task
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print("Factorial:", factorial(int(input("Enter a number: "))))

#recursion
import sys
sys.setrecursionlimit(2000)
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
print(fact(int(input('enter the value: '))))

# wap to create a fun which adds min 2 and max 5 num
def add(a,b,c=0,d=0,e=0):
    return a+b+c+d+e
print(add(2,3,))
print(add(2,3,4,))
print(add(2,3,4,1,))
print(add(2,3,4,1,1))

#wap to find out sum of individual digits in a num
def sum(n):
    sum=0
    while n>0:
        d=n%10
        sum=sum+d
        n=n//10
    return sum
print(sum(int(input('Enter a value: '))))

        