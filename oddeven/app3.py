def findoddeven(num):
    num1=int(num)
    if num1 % 2== 0:
        print("your number "+ num +" is even")
    else:
        print("your number "+ num +" is odd") 

print("Welcome to my Odd even Guess number Game!!!")
number=input("Heyy enter the number:")
findoddeven(number)
