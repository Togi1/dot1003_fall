year=int(input("Year? "))

if year <= 100 and year % 4 == 0:
    print("This year is a leap year.")
elif year > 100 and year < 1000 and year %4 == 0 and year % 100 == 0 :
    print("This year is a leap year")
elif year > 1000 and year % 4 == 0 and year % 100 ==0 and year %  400 == 0:
    print("This year is a leap year")
else:
    print("This year is not a leap year.")