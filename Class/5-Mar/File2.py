# #user-defined functions

def product():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    return a*b
print("The product of the two numbers is: ", product())   
 
   
def prod(a,b):
    return a*b
print(prod(5,6))
print(prod(int(input()), int(input())))


#l1=eval(input("Enter a list of numbers: "))
l1=[-4,-5,-2,-6,-1,1,2,3,4,5]
l2=[]
def task():
    for i in l1:
        if (i<0):
            l2.append(i)
    return l2
print(task())


x = 10
# function
def change_value():
    global x   
    x = 20  
change_value() 
print(x)


def f_name():
    global a
    a=20
    b=2000
    def f_name2():
        nonlocal b
        b=1000
    f_name2()
f_name()
print(a)
print(b)    
    