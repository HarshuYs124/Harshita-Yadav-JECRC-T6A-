# String Methods

s=" hello world "
print(s.upper()) #HELLO
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s="HELLO"
print(s.lower()) #hello
print(s.isupper()) #True

s="HeLLo"
print(s.swapcase()) #hEllO

s="hello world"
print(s.replace("o","a")) #hella warld

s="welcome to the class"
print(s.capitalize()) #Welcome to the class
print(s.title()) #Welcome To The Class
print(s.split()) #['welcome', 'to', 'the', 'class']
print(s.index("m")) #11
print(s.count("o")) #2
print(s.isupper()) #False
print(s.islower()) #True

l=["hello","world","welcome","to","the","class"]
print(" ".join(l)) #hello world welcome to the class

a="1234"
print(a.isdigit()) #True

#List Methods

l=[1,2,3,4,5]
l.append(6) #[1, 2, 3, 4, 5, 6]
l.insert(1,10) #[1, 10, 2, 3, 4, 5]
l.pop() #[1, 2, 3, 4]
l.remove(3) #[1, 2, 4, 5]
print(l) 

l=[5,3,6,2,2,2,1,4]
l.sort() #[1, 2, 3, 4, 5, 6]
print(l.count(2)) #3
print(l) 
print(l.index(6)) #2


#Set Methods 

s={1,2,3,4,5}
s.add(6) 
s.pop()
s.remove(3)
print(s)

a = {1,2,3}
b = {2,3}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
a.clear()
print(a)

#dictionary methods

d={"name":"Harshita","age":21,"city":"Jaipur"}
print(d.keys()) #dict_keys(['name', 'age', 'city'])
print(d.values()) #dict_values(['Harshita', 21, 'Jaipur'])
print(d.items()) #dict_items([('name', 'Harshita'), ('age', 21), ('city', 'Jaipur')])
d.pop("age")
print(d)
print(d.get("name")) #Harshita
d.popitem()
d.update({"country":"India"})
d.clear()
print(d)