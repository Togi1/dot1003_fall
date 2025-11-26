myflag=True
mylisstt=[]
while myflag:
    userinp=input("please enter an input: ")
    if userinp=="exit":
        myflag = False
    else:
        mylisstt.append(userinp)
print(mylisstt)
