a=int(input('Enter the number: '))
haveid=str(input("Do you have an ID card? (yes/no): "))
if a>=18 and haveid == 'yes':
    print("You are eligible.")
else:
    print("You are not eligible.")