#How to print something in python
print("Hello, World!")

#How to find keywords in python
import keyword  
print(keyword.kwlist)

#How to find the value of a variable in python
z = 15
print(z)

#How to find the length of a string in python
my_string = "Hello, World!"
print(len(my_string))

#Multiple variables in one line
a, b, c = 1, 2, 3
a,b,c,d=1,'Harshita',3,True
print(a,b,c,d)

a=b=c=10
print(a)

#How to find id of a variable in python
y = 10  
print(id(y))
a='hi'
print(id(a)) # same id 
b='hi hello'
print(id(b)) # different id
# in hexadecimal
name = 22
mane = 22
print(id(name))
hex(id(name))

#How to find type of a variable in python
x = 5   
print(type(x))

a=2
b=4
c=4.0
d=9.
f=2+3j
g=8-9J
v =False
u =True
print(id(a))
print(id(b))
print(type(a))
print(type(c))
print(type(f))
print(type(v))
