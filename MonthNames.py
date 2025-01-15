#Exercise 1
def get_month_name():
    month = int(input("Enter the month: "))
    if month ==1:
        print("Month 1 is January")
    elif month ==2:
        print("Month 2 is February")
    elif month ==3:
        print("Month 3 is March")
    elif month ==4:
        print("Month 4 is April")
    elif month ==5:
        print("Month 5 is May")
    elif month ==6:
        print("Month 6 is June")
    elif month ==7:
        print("Month 7 is July")
    elif month ==8:
        print("Month 8 is August")
    elif month ==9:
        print("Month 9 is September")
    elif month ==10:
        print("Month 10 is October")
    elif month ==11:
        print("Month 11 is November")
    elif month ==12:
        print("Month 12 is December")
    else:
        print("Invalid month.Please enter a number between 1 and 12.")
get_month_name()

#Exercise 2
age=int(input("Enter your age: "))
full_price= 6

if age <16:
    price=full_price/2
elif age >=60:
    price=full_price/3
else:
    price=6
print(f"Your ticket costs ${price: .2f}")





