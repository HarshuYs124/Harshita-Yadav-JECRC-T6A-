# separators and end in print function

print(10,20,40,'', sep='@')
print(5,10, sep ='@')
print( '#','#',"", sep ='%')
print(1,2,3,sep ='$', end ='^')

#input function
name = input("Enter your name: ")
print("Hello", name)

a = input("Enter a number: ")
print(int(a) + 500)

b= list(input("Enter the values :"))
print(b)

c = eval(input("Enter the values :")) #eval identifies the data type of the input and converts it into that data type
print(c)

#control statements
#if statement
i = 10
if i > 15:
    print("10 is less than 15")
    
#if else statement
i = 20
if i > 0:
    print("i is positive")
else:
    print("i is 0 or Negative")
    
#elif statement
i = 0
if i > 0:
    print("i is positive")
elif i == 0:
    print("i is 0")
else:
    print("i is negative")
    
#nested if statement
i = 10  
if i > 0:
    print("i is positive")
    if i % 2 == 0:
        print("i is even")
    else:
        print("i is odd")
else:
    print("i is 0 or negative")


#loops
#while loop
i = 1
while i <= 5:
    print(i)
    i += 1  
    

#  reverse string with slicing
nums = input("Enter the string: ")
reve = ''
j = len(nums)-1
while j >= 0:
    reve += nums[j]
    j -= 1
print(reve)


# table 
n = int(input("Enter the no: "))
i = 1
while i <=10:
    # print(n, 'x', i, '=', n*i)
    print(f"{n} x {i} = {n*i}")
    i+=1

    
