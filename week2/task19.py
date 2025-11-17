number = int(input("Please type in a number: "))
if number > 0 and number % 2 == 0 :
    print("The number is even")
elif number % 2 != 0 and number > 0  :
    print("The number is odd")
elif number <= 0 :
    print("The number is negative or zero")