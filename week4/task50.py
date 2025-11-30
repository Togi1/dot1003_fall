kulgirdi = input("Please enter string: ")
aranan = input("Please enter search item: ")

aranankonumu = kulgirdi.find(aranan)

if aranankonumu != -1:
    print(f"found it at {aranankonumu}")
else:
    print("not found")