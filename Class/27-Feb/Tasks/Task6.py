num1=eval(input("Enter the first number: "))
op=input("Enter the operator: ")
num2=eval(input("Enter the second number: "))

if op=="+":
    print(num1+num2)    
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    if num2!=0:
        print(num1/num2)
    else:
        print("Error: Division by zero is not allowed.")            