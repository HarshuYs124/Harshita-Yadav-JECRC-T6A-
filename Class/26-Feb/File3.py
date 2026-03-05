#operatore

print(10 and 40)
print(0.0 and 0)
print(10 or 40)
print(0.0 or 2.4)
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(True))
print(bool(''))
print(bool([]))
print(bool(()))
print(bool(set()))
print(bool({}))


i = 2
f = 2.0
c = 3+8j
b = True
l = [1,2,3]
l2 = [7,8,9]
t = (3,4,5)
t2 = (7,8,7,6)
se = {12,23,45}
se2 ={5,6,7}
d = { 'a':23 , 'n': 43}
d2 = { 'pl':234 , 'l': 98}
st = 'aditya'
st2 = '2adf' 

# assigment
t+=t2

# Relational 
print(c > 4+9j)
print(ord('a'))
print(st < st2)
print(l2 > l)
print(l > l2)
print(t == t2)
print( t != l2)
d == d2

# member
print(2 not in l2)
print(3 in t)
# print(23 in se) beacuse it is unorer
print(23 in d)
print('d' in st)

# se == se2
i is f
i is not f

a=10
b=4
print(a/b)
print(a//b)
print(a+b)
print(a-b)
print(a*b)  
print(a**b)
print(a%b)

a = 13
b = 33
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

a = True
b = False
print(a and b)
print(a or b)
print(not a)


a = 10
b = 4
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

a = 10
b = 20
c = a
print(a is not b)
print(a is c)

#boolean values of default values are always false
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(False))





