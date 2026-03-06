# #global var
a=500

# #local var
def fname():
    global a
    a=100
    b=50
    print(a+b)
    def fname2():
        nonlocal b
        b=300
        print (b)
    fname2()
    print(b)
fname()
print(a)

#task

l=[1,2,3,4]
def product():
    p=1
    for pr in l:
        p*=pr
    print(p) 
product()

# write a p to build a initial index of char present in a given SyntaxWarning
# fun(input string, char)
def fun(s,c):
    for i in range(len(s)):
        if s[i] == c:
            return i
print(fun(input("enter a string: "),input("enter a char: ")))

# Packing and Unpacking          
def fun(v,*t):
    for i in range(len(t)):
        if t[i] == v:
            print(t)
            return i
print(fun(100,10,400,50,80,120,100))

def fun(v,*t):
    print(v)
    return t
print(fun(100,10,400,50,80,120,100))
 
 
def fun(**d): 
    return d
print(fun(a=100,b=10,c=400,d=50,e=80,f=120,g=100))
 
    
def fun(a,b,c,d):
    print (a,b,c,d)
fun(*{10:1,20:2,30:3,40:4})
    
    
    