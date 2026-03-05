#pattern printing


#question 1
n=int(input("Enter a number: "))
# m=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1:
            print("*",end="")
        else:
            print(end=" ")
    print()
    
#question 2
n=int(input("Enter a number: "))
for i in range(0,n):
    print(" " * i + "*")
   
#question 3
row=int(input("Enter a number: "))
col=int(input("Enter a number: "))
for i in range(row):
    for j in range(col):
        print("*",end="")
    print()

#question 4
n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(i):
        print("*",end="")
    print()
        
#question 5
n=int(input("Enter a number: "))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()

#question 6
n=int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if i+j<n-1:
            print("*",end="")
        elif i+j==n-1:
            print("#",end="")
        else:
            print("@",end="")
    print()

#question 7
n=int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print("#",end=" ")
        elif i==1 and j==1:
            print("*",end=" ")
        elif i==n-1 and j==n-1:
            print("@",end=" ")   
        else:
            print(end="  ")
    print()