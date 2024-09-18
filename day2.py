#learning data types 
print(len("Hello"))
print("Hello"[0])
print("prakhar"[4])

#string
print("123" + "345")

#integer
print(123 + 345)

#large Integers
print(123_345_789)

#float
print(3.124567)

#boolean
print(True)
print(False)

#type error checking 
print(len("prakhar"))
print(type("Amit"))
print(type(1234))
print(type(12.35))
print(type(True))
print(type(False))

print(int("1234")+int("456"))
print("prakhar"+"singh")

int()
float()
str()
bool()


#mathematiccal operators 
print("My age: " + str(20))
print(123+456)
print(123.56+345.90)
print(True)
print(type(123+745))

print(7-3)
print(8*3)
print(5/10)
print(10//30)
print(2**2)
# (**) operator  is used for the exponent or power

print(3 * 3 + 3 / 3 - 3) #the output is seven

print(3*3/3) #normal method to take the output 3
print(3 * (3 + 3) / 3 - 3) # tbis is a real method for changing the output from 7 to 3

#print((int("7") + (len(input("enter your name"))))

name_of_the_user = input("enter your name: ")
length_of_name=len(name_of_the_user)

print("number of the letter "  +  str(length_of_name))

#number manipulation

rom urllib.request import ftpwrapper

bmi = 84 / 1.65 ** 2
print(bmi)
print((int(bmi)))

print(round(bmi))
print(round(bmi,2))

score =1
print(score)
print("your score is "+ str(score))
print(round(score))

score=12
height=6.1
winning=True
print(f"your score is = {score},your height is {height}, you are winning is {winning}")

#tip calculator project 

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_with_tip=tip / 100 * bill + bill
print(bill_with_tip)
tip_as_percent=tip / 100
total_tip_amount =bill * tip_as_percent
total_bill= bill + total_tip_amount
bill_per_person= total_bill / people
final_amount=round(bill_per_person,2)
print(f"each person should pay: $ {final_amount}")



