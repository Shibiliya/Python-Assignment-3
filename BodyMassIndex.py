#Exercise 3
# weight=float(input("Enter your weight in(kg):"))
# height=float(input("Enter your height in (m):"))
# bmi=weight/(height**2)
# print(f"Your BMI is :{bmi:.2f}")
# if bmi<18.5:
#     print("You are in the 'Underweight' range.")
# elif 18.5 <= bmi <= 24.9:
#     print("You are in the 'Normal' range.")
# elif 25 <= bmi <= 29.9:
#     print("You are in the 'Overweight' range.")
# else:
#     print("You are in the 'Obese' range.")

#Exercise 4
# num1=float(input("Enter the first number: "))
# num2=float(input("Enter the second number: "))
# num3=float(input("Enter the third number: "))
# greatest=max(num1,num2,num3)
# print(f"The greatest number is: {greatest}")

#Exercise 5
# num=int(input("Enter a number: "))
# factorial=1
# for i in range(1,num+1):
#     factorial *= i
# print(f"The factorial of {num} is {factorial}")

#Exercise 6
# num= int(input("Enter a number: "))
# reversed_num=0
# while num >0:
#     digit = num % 10
#     reversed_num=reversed_num * 10+ digit
#     num //=10
# print(f"The reversed number is: {reversed_num}")

#Exercise 7
# number=int(input("Enter a number: "))
# limit=int(input("Enter the limit for multiples: "))
# print(f"The multiples of {number} up to {limit}:")
# for i in range(1,limit + 1):
#     print(number * i)

#Exercise 8
# while True:
#     user_input = input("Enter a value: ")
#     if user_input.lower() == "done":
#         break
#     print(user_input)

#Exercise 9
# for i in range(1,11):
#     if i % 3 ==0 and i % 5 ==0:
#         print("FizzBuzz")
#     elif i % 3 ==0:
#         print("Fizz")
#     elif i % 5 ==0:
#         print("Buzz")
#     else:
#         print(i)

#Exercise 10
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end= " ")
    print ()

