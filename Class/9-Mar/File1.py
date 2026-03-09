# #creating class
# class college:
#     #creating class attributes
#     c_name='jecrc'
#     loc='jaipur'
#     dept='cse'
# #creating object of class 
# s1=college()
# #setting object1 attribute
# s1.name='Harshita'
# s1.loc='delhi'
# s2=college()
# s2.name='Yadav'

# print(s1.name)
# print(s2.name)
# print(s1.loc)

#...
# class College:
#     c_name='jecrc'
#     loc='jaipur'
#     dept='cse'
#     #creating constructor
#     def __init__(self,name,roll,age):
#         self.name=name
#         self.roll=roll
#         self.age=age
#     #creating obj method
#     def display(self):
#         print(self.name,self.roll,self.age,self.c_name,self.loc,self.dept)
    
#     @staticmethod
#     def add(a, b):
#         print("Sum is:", a + b)
        
        
    
#     #creating class method
#     @classmethod
#     def c_disp(cls):
#         print(cls.c_name,cls.loc,cls.dept,sep='\n')
    

# College.add(5,10)      
# s1=College()
# s1.add(4,6)
# s1=College('Harshita','762',21)
# s1.c_disp()
# s2=College('Radha','798',22)

# s2.c_name='poornima'
# s2.display()

# print(s1.c_name)
# print(College.name)


# print(s1.name, s1.roll, s1.age)

# print(s2.name,s2.roll,s2.age)

#...
# types of methods
# 1. object method- we use self argument with these
#can display class attributes using display method by simply add then to display method

# 2. class method
#creating class method
    # @classmethod
    # def c_disp(cls):
    #     print(cls.c_name,cls.loc,cls.dept,sep='\n')
        

# 3. static method

# class College:
#     c_name = 'jecrc'
#     loc = 'jaipur'
#     dept = 'cse'

#     # constructor
#     def __init__(self, name, roll, age):
#         self.name = name
#         self.roll = roll
#         self.age = age

#     # object method
#     def display(self):
#         print(self.name, self.roll, self.age, self.c_name, self.loc, self.dept)

#     # static method
#     @staticmethod
#     def add(a, b):
#         print("Sum is:", a + b)

#     # class method
#     @classmethod
#     def c_disp(cls):
#         print(cls.c_name, cls.loc, cls.dept, sep='\n')


# College.add(5, 10)

# s1 = College("Harshita", 762, 21)

# s1.add(4, 6)


class Student:
    s_name='ABC'
    loc='India'
    def __init__(self,name,roll,sec):
        self.name=name
        self.roll=roll
        self.sec=sec
    @classmethod
    def ch_school(cls,new):
        cls.s_name=new
        
    def display(self):
        print(self.s_name,self.loc)
    
    @classmethod
    def ch_loc(cls,new):
        cls.loc=new
        
    @staticmethod
    def prod():
        a=int(input('a: '))
        b=int(input('b: '))
        return a*b
s1=Student('hello',762,'A')
s2=Student('bye',123,'B')
s3=Student('welcome',234,'c')

              