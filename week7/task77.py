x = int(input("Please enter a number: "))
flag = True

while flag:
    try:
        y = int(input("Please enter divider: "))
        print(f"{x} divided by {y} is {x / y}")
        flag = False
    except ZeroDivisionError:
        print("You can't enter 0 as divider")
    except ValueError:
        print("Invalid Value")
    except Exception:
        print("Some kind of error occurred")