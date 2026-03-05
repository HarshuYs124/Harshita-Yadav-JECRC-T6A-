# datatypes

a=10
b=6.7
c=2+3j
d=True
s='harshita'
print(type(a))
print(type(b))      
print(type(c))
print(type(d))
print(type(s))

#default values
print(int())
print(float())
print(complex())
print(bool())
print(str())

#built in functions
#Absolute function
print(abs(-400))
print(abs(20-400))
# round fucntion
print(round(2.7))
print(round(2,3))
print(round(2.3456,2))
print(round(2.5))
# max built function
print(max(234,45,76,523,47,65))
# min built function
print(min(234,45,76,456,1,23,45))
# Sum built function
sum([1,2,3,4,5])
l1= [1,2,3,43,2,22]
print(sum(l1))

## string and all the uses of '' and " " and ''' '''
a= "it my 'first' string"
print(a)
a

st = ''' hello how are you doing let say can you do "i also want to tel me something " did you eat the lucnh
can we d this
are you there
d'''
print(st)

#length function
ab='my name is harshita'
print(len(ab))

#count function
print(ab.count('a'))
print(ab.count('h'))

#find function
print(ab.find('h'))

#replace function
print(ab.replace('h','H'))

#indexing
print(ab[0])
print(ab[1])

# String method
# String indexing finding
s= "hello this is your Python class everyone"
print(len(s))
# find index of 3rd 'y' in the string
i = s.index('y')
j = s.index('y', i+1)
k = s.index('y', j+1)
print(k)
#find index of 4th 'o' in the string
i = s.index('o')
j = s.index('o', i+1)
k = s.index('o', j+1)
l = s.index('o', k+1)
print(l)

#methods of string
dir(s)
s.isalpha()
s.isdigit()
s.upper()
s.lower()
s.isupper()
s.islower()

