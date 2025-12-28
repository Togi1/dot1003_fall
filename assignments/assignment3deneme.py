gamelist=[]
myflag=True
while myflag:
    userinput=input("Please enter a string: ")
    if userinput!="exit":
        gamelist.append(userinput)
        
    else:
        
        myflag=False
        


def anarya(gamelist):
    return gamelist[::-1]

print(gamelist)
print(anarya(gamelist))
