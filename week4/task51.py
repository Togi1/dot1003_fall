cumle = "The quick brown fox jumps over the lazy dog"
myflag = True

while myflag:
    aranan = input("What are you looking for? ")

    if aranan == "-1":
        print(">Bye.")
        myflag = False

    konum = cumle.find(aranan)

    if konum != -1:
        print(f">found it at {konum}")
    else:
        print(">not found")