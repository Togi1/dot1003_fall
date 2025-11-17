point= int(input("How many points[0-100]"))
if point >= 0 and point <= 49 : 
    print("fail")
elif point >= 50 and point <= 59 :
    print("1")
elif point >= 60 and point <= 69 :
    print("2")
elif point >= 70 and point <= 79 :
    print("3")
elif point >= 80 and point <= 89 :
    print("4")
elif point >= 90 and point <= 100 :
    print("5")
elif point > 100 :
    print("impossible!")
elif point < 0 :
    print("you what?")




