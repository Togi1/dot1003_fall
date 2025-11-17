hourly=float(input("how much do you earn an hour?"))
hour = int(input("How many hours do you work in a day? "))
day = input("Which day do you work of the week? ")

if day == "sunday":
    print(f"daily wages: {hour * hourly * 2}")
else:
    print(f"daily wages: {hour * hourly}")
