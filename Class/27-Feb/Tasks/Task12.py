maths=int(input("Enter the maths marks: "))
science=int(input("Enter the science marks: "))
english=int(input("Enter the english marks: "))
avg=maths+science+english/3
if maths>=40:
    if science>=40:
        if english>=40:
            print("The student has passed")
            if avg>=75:
                print("distinction")
            else:
                print("pass")   
else:
    print("fail") 
      