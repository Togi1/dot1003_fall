def olcum(arg1, arg2):
    if arg1 > arg2:
        return arg1
    elif arg2 > arg1 :
        return arg1
    else:
        print("Their leght are smame")
        return arg1
userinp= input("First word: ")
userinp2=input("Second word: ")
sonuc=olcum(userinp, userinp2)
print(sonuc)