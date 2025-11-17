print("Robin will wear their feathery fire, ");
print("whistling their whims on a low fence-fire");
print("And not one will know of the war,");
print("not one...");




print("Hours in a week")
print(7 * 24 )
print("Minutes in a week")
print(60 * 24 * 7)
print("Seconds in a week ")
print(60* 60 * 7 * 24)

name = input("What is your name?")
email = input("What is your e mail adress?")
nickname = input("What is your nickname")
print("##t's review your information##")
print("Your name:" + name )
print("your e mail adress:" + email )
print("your nickname:" + nickname )
print( name + " | " + email + " | " + nickname )


Name = input ("Name?")
Victim = input ("Victim?")
print("Thank you " + Name + "!")
print("But our " + Name + "is in another castle" +"!")


name1 = "Tolga"
yas = 34
sehir = "Karaman"
print (f"Hi {name}, you are {yas} years old. You live in {sehir}")

name2 = "Tolgahan Ay"
age = 19 
skill1= "python"
level1= "beginner"
skill2= "2d art"
level2= "beginner"
lower = 2000
upper = 3000
print(f"My name is {name2}, I am {age} years old")
print(f"One of my skill is -{skill1} {level1}")
print(f"My another skill is -{skill2} {level2} ")
print(f"My salary expectation is {lower}-{upper} euros")


number1= int(input("Enter your first number: "))
number2= int(input("Enter your second number: "))
print(f"{number1} + {number2} = {number1 + number2}")
print(f"{number1} - {number2} = {number1 - number2}")
print(f"{number1} * {number2} = {number1 * number2}")
print(f"{number1} / {number2} = {number1 / number2}")



Weight= int(input("Enter your weight"))
Height= int(input("Enter your height"))
ans= Weight / (Height / 100) ** 2
print(f"Your BMI is {ans}")




Gamename = input("What is your game's name?")
released= int(input("Which year was this game released?"))
year = int(input("Which year are you in?"))
print(f"{Gamename} is {year - released} years old. ")



number4 = int(input("Please type in the first number: "))
number5 = int(input("Please type in the second number: "))
number6 = int(input("Please type in the third number: "))
product = number4 * number5 * number6
print("The product is", product)




eat_a_week = int(input("How many time a week do you eat at the student cafeteria?"))
prices = int(input("The price of a typical student lunch?"))
how_much_money= int(input("How much money do you spend on groceries in a week?"))

Daily = eat_a_week * prices / 7 + how_much_money / 7
print("Avarage food expenditure:")
print(f"Daily: {eat_a_week * prices / 7 + how_much_money / 7} liras")
print(f"Weekly: {Daily * 7 }")
print(f"Monthly: {Daily * 30 }")