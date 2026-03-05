#slicing
text = "PythonProgramming"
print(text[0:6]) #Python
print(text[6:]) #Programming    
print(text[:6]) #Python
print(text[:]) #PythonProgramming

#using step in slicing
print(text[::2]) #PtoPormig 
print(text[1::2]) #yhnPormn
print(text[::3]) #PhPogm

#negative indexing
print(text[-1]) #g
print(text[-2]) #n
print(text[-6:]) #mming
print(text[:-6]) #PythonProgra


#list
l = ['harshita', 762, '17/07', 21]
print(type(l))
print(list())
print(l[1])
l[1] = 707

# list memory explain
l2 = [100,200, 'hi', 'hello', False]
print(id(l2))
print(id(100))
print(id('hi'))
print(id('hello'))
print(id(l2[3]))
print(id(l2[3][0]))
print(id(l2[3][1]))
print(id(l2[3][2]))
print(id(l2[3][3]))
print(id(l2[3][4]))

#access value in value
print(l2[3][3])

#methods of list
l.append(40)
l.insert(2,'lo')
print(l)
l.remove('lo')
l.pop(4)


lis = ['Python is not easy']
print(lis[0][14])
print(lis[0][-4])
print(lis[0][10])
print(lis[0][-8])
print(lis[0].count('o'))


#tuple
lt = [1]
pl = (2,)
var = ('harshita', 762, 21, 'jecrc')
tup = 1 , 2, 3, 4
print(type(var))
print(type(tup))
print(tuple())
print(type(lt))
print(type(pl))
print(var[0])
print(var[0].count('a'))

#set
st = {1 ,2,3,4,5,6,17,8,15,0}
s = {10, 2.5,(3+2j), 'hi'}
print((st))
print(s)
s.add(20)
print(s)
s.pop()
print(s)
s.remove('hi')
print(s)

s = {1, 2, 3}
s.update([4, 5])
print(s)

#dictonary
d = {'name':'harshita', 'age':21, 'college':'jecrc'}
print(d)
print(d['name'][2])
print(d.get('place'))
print(d.get('name'))
d['age'] = 23
print(d.items())
d['place'] = 'jaipur'
print(d.items())


# practice questionds
a=[10,2j,'python',[2+5j,11,22.22]]
print(a[2])
print(a[-2])
print()

b="Python is hard as well as easy"
b.index('w')

i = len(b)-b.index('w')
print(i)
print(b[18])
print(b[-12])
l =['python','Is','Not','Easy']
print(l[2][0])
print(l[-2][-3])
