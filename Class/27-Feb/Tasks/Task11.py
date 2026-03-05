age=int(input("Enter your age: "))
income=int(input("Enter your income: "))
credit_score=int(input("Enter your credit score: "))

if age>=21:
    if income>=25000:
        if credit_score>=700:
            print("loan approved")
        else:            print("loan rejected (low credit score)")
    else:        print("loan rejected (low income)")     
else:    print("loan rejected (age not eligible)")