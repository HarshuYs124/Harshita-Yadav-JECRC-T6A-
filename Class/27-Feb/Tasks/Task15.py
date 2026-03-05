#for printing the numbers from 1 to 10
i=50
while i>=40:
    print(i)
    i=i-1 

#for printing the sum of first 10 even numbers
i=0
sum=0
while i<20:
    sum+=i
    i=i+2
print(sum)    


#for printing the reverse of a string
i=str(input("Enter the string: "))
index=len(i)-1
rev=""
while index>=0:
    rev+=i[index]
    index=index-1
print(rev)


#for printing the multiplication table of a number
n=1
i=int(input("Enter the number: "))
while n<=10:
    # print(i,'X',n,'=',i*n)
    print(f"{i} X {n} = {i*n}")
    n=n+1
    

for i in range(10,0,-1):
    print(i,end=' ')
