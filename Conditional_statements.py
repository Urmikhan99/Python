# if else
a=13
if a>10:
    print("I will do task A")
else:
    print("I will do tas B")

money=int(input("please provide me the money :- "))
if money == 10:
    print("I will have a coco bar ")
elif money == 20:
    print("I will buy kone")

else:
    print("I will Buy Mango bar")

# Q1. Accept two numbers and print the greatest between them.
num1=int(input("please tell your first number"))
num2=int(input("please tell your 2nd number"))
if num1 >num2:
    print(f"{num1} is greater than {num2}")
elif num2>num1:
    print(f"{num2} is greate than {num1}")
else:
    print(f"{num2} is greater then {num1}")


''' Q2. Accept the gender from the user as char and print the
respective greeting message
Ex - Good Morning Sir (on the basis of gender) '''

gen = input("Please tell your gender as Charecter ( M or F )")
if gen == "M" or gen == "m":
    print("Good morning Sir")

elif gen == "F" or gen == "f":
    print ("Good Morning Mam")

else:
    print("Un")


year = int(input("tell your year :- "))

if year %100 ==0 and year %400 ==0:
    print("its a leap year")
elif year %100 !=0 and year %4 == 0:
    print("its a leap year")
else:
    print("Its a normal year")


# if-elif ladder
t=int(input("tell the temprature :-"))
if t<0:
    print("Freezing Cold")

elif t>=0 and t<10:
    print("very cold")

elif t>=10 and t<20:
    print("cold")

elif t>=20 and t<30:
    print("Plesant")

elif t>=30 and t<40:
    print("hot")

else:
    print("temprature is very hot")