inc=int(input("enter the income: "))

if inc>500000:
    if inc<=1000000:
        print("tax rate is 20% ")
    else:     
        print("tax rate is 30% ")
    
else:    
    if inc>250000:
        print("tax rate is 5% ")
    else:        print("No tax")
