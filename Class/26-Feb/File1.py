#type casting
# int and float
b =5.0

print(int(b))
print(complex(b))
print(bool(b))
print(str(b))

c = 5+2j
print(str(c))
print(bool(c))
print((c))

d =False
print(d)
print(int(d))
print(float(d))
print(complex(d))
print(str(d))

#String datatype
s = 'Harshita'
sa = 'a'
print(bool(s))
print(bool(sa))
print(list(s))
print(list(sa))
print(tuple(s))
print(tuple(sa))
print(set(s))
print(set(sa))

# string type cast
z = '123'
print(int(z))
print(float(z))
print(complex(z))
print(bool(z))
print(list(z))
print(tuple(z))
print(set(z))

y= '123.34'
print(float(y))
print(complex(y))
print(bool(y))
print(list(y))
print(tuple(y))
print(set(y))

u = '2+4j'
print(bool(u))
print(list(u))
print(tuple(u))
print(set(u))

# List type casting
li = [1,2,'hi',2,3,3,4]
print(bool(li))
print(list(li))
print(tuple(li))
print(set(li))

l2 = ['hi', [2,23],'to',['hi','hello']]
print(dict(l2))
print(bool(l2))
print(list(l2))
print(tuple(l2))

l3 =['hi','lo','pp']
print(dict(l3))
print(bool(l3))
print(list(l3))
print(tuple(l3))
print(set(l3))

# tuples typecasting
t1 = ([1,2],(3,4),'hi')
print(str(t1))
print(dict(t1))
print(bool(t1))
print(list(t1))
print(tuple(t1))
print(set(t1))

# set typecasting
s1 = {1,2,3,(4,5),2}
s2 ={'hi','lo','pp'}
print(str(s1))
print(dict(s2))
print(bool(s1))
print(list(s1))
print(tuple(s1))

# dictory typecasting
d1 = { 1:45, 'name':'aditya'}
d2 = { 'list': [1,2],1:2}
print(d2)
print(str(d1))
print(bool(d1))
print(list(d1))
print(tuple(d1))
print(set(d1))

# for values of the dict in typecasting 
print(list(d1.values()))
print(tuple(d1.values()))
print(set(d1.values()))
# for both values and key of the dict 
print(list(d1.items()))
print(tuple(d1.items()))
print(set(d1.items()))

